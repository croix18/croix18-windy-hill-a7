#!/usr/bin/env python3
"""pdf → text that keeps exponents. Spans that are smaller than the line's main font and raised
above its baseline are written as ^{...}; lowered ones as _{...}. Usage: pdf_supertext.py in.pdf > out.txt"""
import pymupdf,sys
doc=pymupdf.open(sys.argv[1])
for pno,page in enumerate(doc,1):
    print(f"\n===== page {pno} =====")
    d=page.get_text("dict")
    lines=[]
    for b in d["blocks"]:
        for l in b.get("lines",[]):
            spans=[s for s in l["spans"] if s["text"].strip()!="" or s["text"]==" "]
            if not spans: continue
            main=max((s["size"] for s in spans), default=0)
            base=max((s["origin"][1] for s in spans if s["size"]>=main-0.5), default=spans[0]["origin"][1])
            out=""
            for s in spans:
                t=s["text"]
                if s["size"]<main-1.5 and s["origin"][1]<base-1.0: t="^{"+t.strip()+"}"
                elif s["size"]<main-1.5 and s["origin"][1]>base+1.0: t="_{"+t.strip()+"}"
                out+=t
            lines.append((round(l["bbox"][1]),l["bbox"][0],out))
    lines.sort()
    cury=None; row=[]
    for y,x,t in lines:
        if cury is not None and abs(y-cury)<=3: row.append((x,t))
        else:
            if row: print("   ".join(t for x,t in sorted(row)))
            row=[(x,t)]; cury=y
    if row: print("   ".join(t for x,t in sorted(row)))
