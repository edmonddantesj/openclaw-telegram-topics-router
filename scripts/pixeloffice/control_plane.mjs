#!/usr/bin/env node
/**
 * PixelOffice Local Control Plane (minimal)
 * - HTTP ingest: POST /event
 * - HTTP state:  GET /state
 * - WS broadcast: ws://127.0.0.1:4100
 *
 * Purpose: SwarmWatch-style local-first event bus for PixelOffice overlay.
 *
 * Dependency: ws
 *   npm i ws
 */

import http from 'node:http';
import { WebSocketServer } from 'ws';

const HOST = process.env.PIXELOFFICE_HOST || '127.0.0.1';
const PORT = Number(process.env.PIXELOFFICE_PORT || 4100);

/** @type {Record<string, any>} */
const stateByAgentKey = {};

function agentKeyOf(ev) {
  return ev.agentKey || `${ev.agentFamily}:${ev.agentInstanceId}`;
}

function nowSec() {
  return Math.floor(Date.now() / 1000);
}

function safeJson(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, {
    'content-type': 'application/json; charset=utf-8',
    'content-length': Buffer.byteLength(body),
  });
  res.end(body);
}

const server = http.createServer(async (req, res) => {
  try {
    if (!req.url) return safeJson(res, 404, { ok: false });

    if (req.method === 'GET' && req.url === '/health') {
      return safeJson(res, 200, { ok: true, ts: nowSec() });
    }

    if (req.method === 'GET' && req.url === '/state') {
      return safeJson(res, 200, stateByAgentKey);
    }

    if (req.method === 'POST' && req.url === '/event') {
      const chunks = [];
      for await (const c of req) chunks.push(c);
      const raw = Buffer.concat(chunks).toString('utf-8');
      const ev = JSON.parse(raw);

      if (ev?.type !== 'agent_state') {
        return safeJson(res, 400, { ok: false, error: 'unsupported_type' });
      }
      if (!ev.agentFamily || !ev.agentInstanceId || !ev.agentName || !ev.state) {
        return safeJson(res, 400, { ok: false, error: 'missing_fields' });
      }

      const key = agentKeyOf(ev);
      const normalized = { ...ev, agentKey: key, ts: ev.ts || nowSec() };
      stateByAgentKey[key] = normalized;

      // broadcast
      const msg = JSON.stringify(normalized);
      for (const client of wss.clients) {
        if (client.readyState === 1) client.send(msg);
      }

      return safeJson(res, 200, { ok: true, agentKey: key });
    }

    return safeJson(res, 404, { ok: false, error: 'not_found' });
  } catch (e) {
    return safeJson(res, 500, { ok: false, error: 'server_error', message: String(e?.message || e) });
  }
});

const wss = new WebSocketServer({ server });

wss.on('connection', (ws) => {
  // on connect: send snapshot
  for (const ev of Object.values(stateByAgentKey)) {
    ws.send(JSON.stringify(ev));
  }
});

server.listen(PORT, HOST, () => {
  console.log(`[pixeloffice-control-plane] listening on http://${HOST}:${PORT}`);
});
