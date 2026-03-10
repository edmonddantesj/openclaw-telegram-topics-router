from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup

CATEGORY_PATTERNS = {
    "decision": [
        r"\b결정\b", r"\b확정\b", r"\b원칙\b", r"\b정책\b", r"\brule\b", r"\bmust\b",
        r"\bshall\b", r"\b결론\b", r"\b기준\b", r"\bprotocol\b", r"\b아키텍처\b",
    ],
    "task": [
        r"\btodo\b", r"\btask\b", r"\b해야\b", r"\b진행해\b", r"\b해줘\b", r"\b작업\b",
        r"\b수정\b", r"\b정리\b", r"\b복원\b", r"\b추가\b", r"\b점검\b", r"\b구현\b",
    ],
    "deliverable": [
        r"\b산출물\b", r"\bdeliverable\b", r"\boutput\b", r"\b초안\b", r"\b문서\b",
        r"\bdb\b", r"\bssot\b", r"\bnotion\b", r"\bpr\b", r"\b스크립트\b",
    ],
    "status": [
        r"\bstatus\b", r"\b상태\b", r"\b완료\b", r"\b진행중\b", r"\bblocked\b", r"\b보류\b",
        r"\b정상\b", r"\b오류\b", r"\b실패\b", r"\b성공\b", r"\b가능\b", r"\b불가\b",
    ],
}

CONFLICT_PATTERNS = [r"\bconflict\b", r"\b충돌\b", r"\b상충\b", r"\boverwrite\b"]
UNCERTAIN_PATTERNS = [r"\buncertain\b", r"\b불확실\b", r"\bmaybe\b", r"\b추정\b", r"\b가정\b", r"\b확인 필요\b"]
UPSTREAM_RELEVANCE_PATTERNS = [
    r"\bacp\b", r"claude code", r"codex", r"openclaw", r"session", r"subagent", r"agent", r"thread",
]


@dataclass
class Msg:
    source: str
    html_file: str
    msg_id: str
    ts: str
    author: str
    text: str
    ref: str


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def parse_html(path: Path, source: str) -> list[Msg]:
    soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    msgs: list[Msg] = []
    for div in soup.select("div.message"):
        msg_id = div.get("id", "")
        body = div.select_one("div.body")
        if not body:
            continue
        author_el = body.select_one("div.from_name")
        date_el = body.select_one("div.pull_right.date.details")
        text_el = body.select_one("div.text")
        if not date_el or not text_el:
            continue
        author = normalize_text(author_el.get_text(" ", strip=True) if author_el else "") or "(unknown)"
        text = normalize_text(text_el.get_text(" ", strip=True))
        if not text:
            continue
        ts = date_el.get("title", "")
        ref = f"{path.name}#{msg_id}"
        msgs.append(Msg(source=source, html_file=str(path), msg_id=msg_id, ts=ts, author=author, text=text, ref=ref))
    return msgs


def classify(text: str) -> list[str]:
    hits = []
    lowered = text.lower()
    for category, pats in CATEGORY_PATTERNS.items():
        if any(re.search(p, lowered, re.I) for p in pats):
            hits.append(category)
    return hits


def is_relevant_upstream(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(p, lowered, re.I) for p in UPSTREAM_RELEVANCE_PATTERNS)


def flags(text: str) -> list[str]:
    lowered = text.lower()
    out = []
    if any(re.search(p, lowered, re.I) for p in CONFLICT_PATTERNS):
        out.append("conflict")
    if any(re.search(p, lowered, re.I) for p in UNCERTAIN_PATTERNS):
        out.append("uncertain")
    return out


def main() -> None:
    root = Path('/Users/silkroadcat/.openclaw/workspace/_restore/acp_20260310')
    a_root = root / 'raw/topic_A_current'
    b_root = root / 'raw/dm_B_upstream'
    out = root / 'structured'
    out.mkdir(parents=True, exist_ok=True)

    a_msgs: list[Msg] = []
    for p in sorted(a_root.rglob('messages*.html')):
        a_msgs.extend(parse_html(p, 'A_current_topic_truth'))
    b_msgs: list[Msg] = []
    for p in sorted(b_root.rglob('messages*.html')):
        b_msgs.extend(parse_html(p, 'B_upstream_context'))

    (out / 'parsed_A_current_topic_truth.jsonl').write_text('\n'.join(json.dumps(asdict(m), ensure_ascii=False) for m in a_msgs), encoding='utf-8')
    (out / 'parsed_B_upstream_context.jsonl').write_text('\n'.join(json.dumps(asdict(m), ensure_ascii=False) for m in b_msgs), encoding='utf-8')

    a_structured = []
    b_proposals = []
    flagged = []

    for m in a_msgs:
        cats = classify(m.text)
        if not cats:
            continue
        rec = {
            'layer': 'structured',
            'mode': 'current_topic_truth',
            'source': m.source,
            'categories': cats,
            'proposal_only': False,
            'author': m.author,
            'timestamp': m.ts,
            'text': m.text,
            'source_ref': m.ref,
        }
        a_structured.append(rec)
        fs = flags(m.text)
        if fs:
            flagged.append(rec | {'flags': fs})

    for m in b_msgs:
        if not is_relevant_upstream(m.text):
            continue
        cats = classify(m.text)
        if not cats:
            continue
        rec = {
            'layer': 'structured',
            'mode': 'proposal_only',
            'source': m.source,
            'categories': cats,
            'proposal_only': True,
            'author': m.author,
            'timestamp': m.ts,
            'text': m.text,
            'source_ref': m.ref,
        }
        b_proposals.append(rec)
        fs = flags(m.text)
        if fs:
            flagged.append(rec | {'flags': fs})

    def write_jsonl(path: Path, records: Iterable[dict]):
        path.write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in records), encoding='utf-8')

    write_jsonl(out / 'TOPIC_BACKUP_ACP_20260310.jsonl', a_structured)
    write_jsonl(out / 'DM_BACKUP_CHEONGMYO_1TO1_20260310.jsonl', b_proposals)
    write_jsonl(out / 'conflict_uncertain_ACP_20260310.jsonl', flagged)

    # category-specific proposal files from upstream
    for cat in ['decision', 'task', 'deliverable', 'status']:
        write_jsonl(out / f'PROPOSAL_ACP_{cat.upper()}_20260310.jsonl', [r for r in b_proposals if cat in r['categories']])

    manifest = {
        'created_at': datetime.now().isoformat(),
        'topic_key': 'ACP',
        'labels': [
            'TOPIC_BACKUP_ACP_20260310',
            'DM_BACKUP_CHEONGMYO_1TO1_20260310',
            'RAW_TOPIC_BACKUP_ACP_20260310',
            'RAW_DM_BACKUP_CHEONGMYO_1TO1_20260310',
            'PROPOSAL_ACP_[DECISION|TASK|DELIVERABLE|STATUS]_20260310',
        ],
        'counts': {
            'a_messages': len(a_msgs),
            'b_messages': len(b_msgs),
            'a_structured': len(a_structured),
            'b_proposals': len(b_proposals),
            'flagged_conflict_or_uncertain': len(flagged),
        },
        'notes': [
            'A is treated as current-topic truth.',
            'B is treated as upstream context.',
            'No direct apply/overwrite performed.',
            'B-derived structured records remain proposal_only.',
        ],
    }
    (out / 'manifest_ACP_20260310.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
