#!/usr/bin/env node
/**
 * Tag normalized_messages.jsonl with topic labels using keyword rules.
 * Output: artifacts/telegram_ingest/tagged_messages.jsonl
 */
import fs from 'fs';

const inPath = process.argv[2] || 'artifacts/telegram_ingest/normalized_messages.jsonl';
const rulesPath = process.argv[3] || 'tools/topic_tagging_rules.json';
const outPath = process.argv[4] || 'artifacts/telegram_ingest/tagged_messages.jsonl';

const rules = JSON.parse(fs.readFileSync(rulesPath,'utf8'));
const ruleList = Object.entries(rules).map(([topic, kws])=>({topic, kws: kws.map(k=>k.toLowerCase())}));

function score(text){
  const t = (text||'').toLowerCase();
  const scores = {};
  for (const {topic, kws} of ruleList){
    let s=0;
    for (const k of kws){
      if (!k) continue;
      if (t.includes(k)) s++;
    }
    if (s>0) scores[topic]=s;
  }
  const sorted = Object.entries(scores).sort((a,b)=>b[1]-a[1]);
  return {scores, top: sorted.slice(0,3)};
}

import path from 'path';
fs.mkdirSync(path.dirname(outPath), {recursive:true});
const lines = fs.readFileSync(inPath,'utf8').split('\n').filter(Boolean);
const out = fs.createWriteStream(outPath, {flags:'w'});

for (const line of lines){
  const rec = JSON.parse(line);
  const basis = [rec.text, rec.from, rec.file, JSON.stringify(rec.media||[])].join('\n');
  const {scores, top} = score(basis);
  const tags = top.map(([t])=>t);
  const confidence = top.length? top[0][1] : 0;
  out.write(JSON.stringify({...rec, tags, tagScores: scores, tagConfidence: confidence})+'\n');
}
out.end();
console.error(`Tagged ${lines.length} messages -> ${outPath}`);
