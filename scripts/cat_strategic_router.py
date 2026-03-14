#!/usr/bin/env python3
import json, re, sys
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

STRATEGIC = [
    '전략','방향','방향성','사업구조','수익화','장기','포지셔닝','큰 그림','구조','시장',
    '맞아?','타당','판단','리스크','우려','왜', '브랜드'
]
EXECUTION = [
    '실행','운영','우선순위','정리','붙이지','도입','어떻게','바로','구현','적용','단계','로드맵','체계'
]
MULTI = ['둘이 논의해','둘이 얘기해','둘 다','같이 봐','같이 이야기','둘이 봐']
CHEONGMYO = ['청묘']
HEUKMYO = ['흑묘']


def contains_any(text, arr):
    return any(x in text for x in arr)


def score(text, arr):
    return sum(1 for x in arr if x in text)


def is_night(now=None):
    now = now or datetime.now(KST)
    return now.hour >= 23 or now.hour < 8


def classify(message, reply_to_agent=None, tagged_agents=None, now=None):
    text = (message or '').strip()
    tagged_agents = tagged_agents or []
    night = is_night(now)

    # Priority 1: direct tag
    if '청묘' in tagged_agents:
        return {'mode':'single','owner':'청묘','secondary':None,'reason':'direct-tag','night_mode':night,'confidence':'high'}
    if '흑묘' in tagged_agents:
        return {'mode':'single','owner':'흑묘','secondary':None,'reason':'direct-tag','night_mode':night,'confidence':'high'}

    # Priority 2: reply target
    if reply_to_agent in ('청묘','흑묘'):
        return {'mode':'single','owner':reply_to_agent,'secondary':None,'reason':'reply-target','night_mode':night,'confidence':'high'}

    # Priority 3: explicit multi-call
    if contains_any(text, MULTI) or (('청묘' in text) and ('흑묘' in text)):
        strategic_score = score(text, STRATEGIC)
        execution_score = score(text, EXECUTION)
        owner = '흑묘' if strategic_score > execution_score else '청묘'
        secondary = '청묘' if owner == '흑묘' else '흑묘'
        return {'mode':'dual','owner':owner,'secondary':secondary,'reason':'explicit-multi-call','night_mode':night,'confidence':'high'}

    # Priority 4/5: role split
    strategic_score = score(text, STRATEGIC)
    execution_score = score(text, EXECUTION)
    if strategic_score == 0 and execution_score == 0 and len(text) <= 6:
        return {'mode':'silent','owner':None,'secondary':None,'reason':'low-value/no-action','night_mode':night,'confidence':'medium'}

    if strategic_score > execution_score:
        return {'mode':'single','owner':'흑묘','secondary':None,'reason':'strategic-question','night_mode':night,'confidence':'medium'}
    if execution_score > strategic_score:
        return {'mode':'single','owner':'청묘','secondary':None,'reason':'execution-question','night_mode':night,'confidence':'medium'}

    # fallback
    return {'mode':'single','owner':'청묘','secondary':None,'reason':'fallback-cheongmyo','night_mode':night,'confidence':'low'}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        payload = json.loads(sys.argv[1])
    else:
        payload = json.load(sys.stdin)
    result = classify(
        payload.get('message',''),
        reply_to_agent=payload.get('reply_to_agent'),
        tagged_agents=payload.get('tagged_agents',[]),
    )
    print(json.dumps(result, ensure_ascii=False))
