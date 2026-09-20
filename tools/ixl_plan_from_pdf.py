"""Parse IXL's printed skill plan PDF (Print skill plan button) into a7/reference/ixl_skills_by_lesson.json.
Lessons that share one rule-bounded block in the PDF share the same skills. Usage: python3 tools/ixl_plan_from_pdf.py [pdf]"""
import pymupdf,re,json
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
doc=pymupdf.open(sys.argv[1] if len(sys.argv)>1 else os.path.join(HERE,'..','a7','reference','sources','IXL skill plan - Math Nation Accelerated Grade 7 (printed 2026).pdf'))
groups=[]
for pno,page in enumerate(doc):
    if pno==0: continue
    # horizontal rules: drawings that are thin wide rects/lines in the table
    rules=[]
    for d in page.get_drawings():
        r=d['rect']
        if r.width>300 and r.height<3 and 100<r.y0<1000: rules.append(r.y0)
    rules=sorted(set(round(y,1) for y in rules))
    # collect lines with y, x, text
    lines=[]
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            txt=''.join(s['text'] for s in l['spans']).strip()
            if not txt: continue
            x=l['bbox'][0]; y=(l['bbox'][1]+l['bbox'][3])/2
            lines.append((y,x,txt))
    lines.sort()
    def band(y):
        i=0
        for r in rules:
            if r<y: i+=1
        return i
    cells={}
    for y,x,t in lines:
        if re.match(r'Visit IXL|©|Math Nation: Florida|^p\. \d+|Unit \d+$',t) or t in ('Textbook section','IXL skills'): continue
        cells.setdefault(band(y),[]).append((y,x,t))
    for bidx in sorted(cells):
        items=cells[bidx]
        lessons=[m.group(1) for y,x,t in items if x<300 for m in [re.match(r'^Lesson (\d+\.\d+):',t)] if m]
        right=[(y,t) for y,x,t in items if x>=300]
        if not lessons:
            if not right: continue
            g=groups[-1]; print('continuation into',g['lessons'],[t for y,t in right]); mode='also' if g['also'] else 'main'
        else:
            g={'lessons':lessons,'main':[],'also':[]}; groups.append(g); mode='main'
        skills=[]; cur=None
        def complete(): return cur is not None and re.search(r'\s[A-Z0-9]{3}$',cur[1])
        for y,t in right:
            if t=='Also consider': mode='also'; continue
            if t=='•': continue
            if re.match(r'^\d+\.\s',t) or cur is None or complete():
                cur=[mode,re.sub(r'^\d+\.\s*','',t)]; skills.append(cur)
            else:
                cur[1]+=' '+t
        for m,txt in skills:
            txt=' '.join(txt.split())
            mm=re.match(r'^(.*?)\s+([A-Z0-9]{3})$',txt)
            if not mm: raise SystemExit(f"no code p{pno+1}: {txt}")
            g[m].append({'name':mm.group(1).replace('- ','-'),'code':mm.group(2)})
out={}
for g in groups:
    for lid in g['lessons']:
        assert lid not in out, lid
        out[lid]={'main':g['main'],'also':g['also']}
json.dump(out,open(os.path.join(HERE,'..','a7','reference','ixl_skills_by_lesson.json'),'w'),indent=1)
print(len(out))
for g in groups:
    if len(g['lessons'])>1: print('shared',g['lessons'],[s['code'] for s in g['main']],[s['code'] for s in g['also']])
print('empty',[k for k,v in out.items() if not v['main'] and not v['also']])
