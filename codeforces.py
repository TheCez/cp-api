import requests as r
import json

def present():
    url = 'https://codeforces.com/api/contest.list'
    comp = r.get(url)
    comp = (comp.text[24:-1])
    res = json.loads(comp)
    out = []
    for i in res:
        if(i['phase']=='BEFORE'):
            out.append(i)
        else:
            break
    return out

def past():
    url = 'https://codeforces.com/api/contest.list'
    comp = r.get(url)
    comp = (comp.text[24:-1])
    res = json.loads(comp)
    out = []
    for i in res:
        if(i['phase']=='FINISHED'):
            out.append(i)
    return out