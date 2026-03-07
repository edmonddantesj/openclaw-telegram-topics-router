#!/usr/bin/env node
/**
 * PixelOffice watcher → emits normalized agent_state events to local control plane.
 *
 * Watches:
 * - HF files under context/handoff/HF_*.md
 * - launchd logs under logs/launchd_*.out.log
 *
 * No external deps (uses fs.watch + small tail polling).
 */

import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.env.PIXELOFFICE_ROOT || path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const CP = process.env.PIXELOFFICE_CP || 'http://127.0.0.1:4100';

const HF_DIR = path.join(ROOT, 'context/handoff');
const LOG_DIR = path.join(ROOT, 'logs');

function nowSec() { return Math.floor(Date.now() / 1000); }

async function postEvent(ev) {
  const r = await fetch(`${CP}/event`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(ev),
  });
  if (!r.ok) {
    const t = await r.text().catch(()=>'');
    console.error('[emit] failed', r.status, t);
  }
}

function parseHFStatus(text) {
  const m = text.match(/^- \*\*Status:\*\*\s*(ACTIVE|HOLD|DONE)\s*$/m);
  return m ? m[1] : 'ACTIVE';
}

function stateFromHFStatus(status) {
  if (status === 'DONE') return 'done';
  if (status === 'HOLD') return 'idle';
  return 'running';
}

async function emitHF(filePath) {
  const base = path.basename(filePath);
  const slug = base.replace(/^HF_/, '').replace(/\.md$/, '');
  const text = fs.readFileSync(filePath, 'utf-8');
  const status = parseHFStatus(text);

  const ev = {
    type: 'agent_state',
    agentFamily: 'pixeloffice',
    agentInstanceId: `hf:${slug}`,
    agentName: `HF ${slug}`,
    state: stateFromHFStatus(status),
    detail: status,
    hook: 'hf_update',
    projectName: 'aoineco',
    ts: nowSec(),
    meta: { hfPath: path.relative(ROOT, filePath) },
  };
  await postEvent(ev);
}

// crude tailer for log files
const lastSizes = new Map();
async function pollLogs() {
  let files = [];
  try {
    files = fs.readdirSync(LOG_DIR)
      .filter(f => f.startsWith('launchd_') && f.endsWith('.out.log'))
      .map(f => path.join(LOG_DIR, f));
  } catch {
    return;
  }

  for (const fp of files) {
    try {
      const st = fs.statSync(fp);
      const prev = lastSizes.get(fp) ?? 0;
      if (st.size > prev) {
        lastSizes.set(fp, st.size);
        const label = path.basename(fp).replace(/^launchd_/, '').replace(/\.out\.log$/, '');
        await postEvent({
          type: 'agent_state',
          agentFamily: 'pixeloffice',
          agentInstanceId: `launchd:${label}`,
          agentName: `launchd ${label}`,
          state: 'done',
          detail: 'tick',
          hook: 'launchd_tick',
          projectName: 'aoineco',
          ts: nowSec(),
          meta: { proof: [{ kind: 'log', value: path.relative(ROOT, fp) }] },
        });
      } else {
        lastSizes.set(fp, st.size);
      }
    } catch {}
  }
}

function watchHFDir() {
  // emit initial snapshot
  const hfs = fs.readdirSync(HF_DIR).filter(f => f.startsWith('HF_') && f.endsWith('.md'));
  for (const f of hfs) emitHF(path.join(HF_DIR, f)).catch(()=>{});

  fs.watch(HF_DIR, { persistent: true }, (eventType, filename) => {
    if (!filename) return;
    if (!filename.startsWith('HF_') || !filename.endsWith('.md')) return;
    const fp = path.join(HF_DIR, filename);
    // debounce via next tick
    setTimeout(() => {
      if (fs.existsSync(fp)) emitHF(fp).catch(console.error);
    }, 150);
  });
}

async function main() {
  console.log('[pixeloffice-watch] root=', ROOT);
  console.log('[pixeloffice-watch] controlPlane=', CP);
  console.log('[pixeloffice-watch] watching HF + polling logs');

  watchHFDir();
  setInterval(() => pollLogs().catch(()=>{}), 2000);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
