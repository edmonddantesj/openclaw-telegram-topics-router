#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const ROOT = '/Users/silkroadcat/.openclaw/workspace';
const statePath = path.join(ROOT, 'artifacts/radar/radar_state.json');
fs.mkdirSync(path.dirname(statePath), { recursive: true });

let state = { lastRunAt: null };
if (fs.existsSync(statePath)) state = JSON.parse(fs.readFileSync(statePath, 'utf8'));

const now = Date.now();
const WEEK = 7 * 24 * 60 * 60 * 1000;
const due = !state.lastRunAt || (now - new Date(state.lastRunAt).getTime()) >= WEEK;

if (!due) {
  console.log('skipped');
  process.exit(0);
}

const out = execFileSync('node', [path.join(ROOT, 'scripts/radar/radar_scan_github.mjs')], { encoding: 'utf8' });
state.lastRunAt = new Date().toISOString();
state.lastReport = out.trim();
fs.writeFileSync(statePath, JSON.stringify(state, null, 2));
console.log(out.trim());
