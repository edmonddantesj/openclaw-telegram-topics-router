#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const ROOT = '/Users/silkroadcat/.openclaw/workspace';
const watchlistPath = path.join(ROOT, 'context/research/radar/WATCHLIST_v0_1.json');
const reportDir = path.join(ROOT, 'context/research/radar');
const artDir = path.join(ROOT, 'artifacts/radar');
const today = new Date().toISOString().slice(0, 10).replace(/-/g, '');
const dayDashed = new Date().toISOString().slice(0, 10);

fs.mkdirSync(reportDir, { recursive: true });
fs.mkdirSync(artDir, { recursive: true });

const watch = JSON.parse(fs.readFileSync(watchlistPath, 'utf8'));
const results = [];

for (const query of watch.queries.slice(0, 8)) {
  try {
    const out = execFileSync('gh', [
      'search', 'repos', query,
      '--limit', '5',
      '--json', 'name,owner,description,url,updatedAt,stargazersCount'
    ], { encoding: 'utf8' });
    const parsed = JSON.parse(out);
    results.push({ query, items: parsed });
  } catch (e) {
    results.push({ query, error: String(e) });
  }
}

const artPath = path.join(artDir, `radar_${today}_${Date.now()}.json`);
fs.writeFileSync(artPath, JSON.stringify({ generatedAt: new Date().toISOString(), results }, null, 2));

const md = [];
md.push(`# AOI Core Radar Report — ${dayDashed}`);
md.push('');
md.push('- scope: GitHub benchmark radar');
md.push(`- watchlist: \`context/research/radar/WATCHLIST_v0_1.json\``);
md.push(`- artifact: \`${artPath}\``);
md.push('');
for (const row of results) {
  md.push(`## Query: ${row.query}`);
  if (row.error) {
    md.push(`- error: ${row.error}`);
  } else {
    for (const item of row.items.slice(0, 3)) {
      const owner = item.owner?.login || 'owner';
      md.push(`- ${owner}/${item.name} — ${item.description || '(no description)'} — ${item.url}`);
    }
  }
  md.push('');
}

const reportPath = path.join(reportDir, `REPORT_${today}.md`);
fs.writeFileSync(reportPath, md.join('\n'));
console.log(reportPath);
