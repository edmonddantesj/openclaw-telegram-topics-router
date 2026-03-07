#!/usr/bin/env node
/**
 * Parse Telegram Desktop HTML export (messages*.html) into JSONL.
 * No external deps.
 *
 * Output schema (one line per message):
 * {file, msgId, date, from, text, hasMedia, media:[{type, href, name}]}
 */
import fs from 'fs';
import path from 'path';

const root = process.argv[2];
if (!root) {
  console.error('Usage: node tools/telegram_export_parse.mjs <export_dir>');
  process.exit(2);
}

function walk(dir) {
  const out = [];
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
}

const files = walk(root).filter(f => /messages\d*\.html$/i.test(path.basename(f)) || path.basename(f)==='messages.html');
files.sort((a,b)=>a.localeCompare(b, undefined, {numeric:true, sensitivity:'base'}));

function stripHtml(s) {
  return s
    .replace(/<br\s*\/?\s*>/gi, '\n')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/\s+$/g, '')
    .replace(/^\s+/g, '');
}

let msgSeq = 0;
const outPath = path.join('artifacts/telegram_ingest', 'normalized_messages.jsonl');
fs.mkdirSync(path.dirname(outPath), { recursive: true });
const out = fs.createWriteStream(outPath, { flags: 'w' });

for (const f of files) {
  const html = fs.readFileSync(f, 'utf8');

  // Split by message blocks
  const blocks = html.split(/<div class="message (?:default clearfix|service)"/g);
  // first block is header
  for (let i=1;i<blocks.length;i++) {
    const b = '<div class="message '+blocks[i];

    // date
    const dateM = b.match(/<div class="date">\s*([^<]+?)\s*<\/div>/i);
    const date = dateM ? stripHtml(dateM[1]) : null;

    // from
    const fromM = b.match(/<div class="from_name">([\s\S]*?)<\/div>/i);
    const from = fromM ? stripHtml(fromM[1]) : null;

    // text (may appear multiple times; prefer the first .text)
    const textM = b.match(/<div class="text">([\s\S]*?)<\/div>/i);
    const text = textM ? stripHtml(textM[1]) : '';

    // message id if present
    const idM = b.match(/<a class="message__date" href="#go_to_message(\d+)"/i) || b.match(/go_to_message(\d+)/i);
    const msgId = idM ? idM[1] : String(++msgSeq);

    // media links
    const media = [];
    const linkRe = /<a[^>]+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi;
    let m;
    while ((m = linkRe.exec(b))) {
      const href = m[1];
      if (!href || href.startsWith('#')) continue;
      const name = stripHtml(m[2] || '');
      if (href.includes('files/') || href.includes('photos/') || href.includes('video_files/')) {
        let type = 'file';
        if (href.includes('photos/')) type = 'photo';
        if (href.includes('video_files/')) type = 'video';
        media.push({ type, href, name });
      }
    }

    const rec = {
      file: path.relative(process.cwd(), f),
      msgId,
      date,
      from,
      text,
      hasMedia: media.length > 0,
      media
    };
    out.write(JSON.stringify(rec) + '\n');
  }
}

out.end();
console.error(`Wrote ${outPath} from ${files.length} html files.`);
