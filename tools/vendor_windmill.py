#!/usr/bin/env python3
"""Copy what the decks need from the Windmill repository (the shared contract) into
a7/build/assets/windmill/, recording the commit it came from.

    python3 tools/vendor_windmill.py [path/to/Windmill]     (default: ../Windmill or ../windmill)

Brings: room-reader.js (as is), spine.json (wrapped as spine.js: `window.SPINE = …`), benchmarks.json.
Nothing here is edited by hand; change it in Windmill and vendor again. BUILDING A UNIT §5b.
"""
import json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, ".."))
DEST = os.path.join(ROOT, "a7", "build", "assets", "windmill")
cands = [sys.argv[1]] if len(sys.argv) > 1 else [os.path.join(ROOT, "..", "Windmill"), os.path.join(ROOT, "..", "windmill")]
src = next((os.path.abspath(c) for c in cands if os.path.isdir(c)), None)
if not src:
    sys.exit("vendor_windmill: no Windmill checkout found; pass its path")
os.makedirs(DEST, exist_ok=True)
shutil.copy2(os.path.join(src, "room", "room-reader.js"), os.path.join(DEST, "room-reader.js"))
shutil.copy2(os.path.join(src, "room", "benchmarks.json"), os.path.join(DEST, "benchmarks.json"))
spine = json.load(open(os.path.join(src, "spine", "spine.json"), encoding="utf-8"))
with open(os.path.join(DEST, "spine.js"), "w", encoding="utf-8") as f:
    f.write("window.SPINE = " + json.dumps(spine, ensure_ascii=False, separators=(",", ":")) + ";\n")
head = subprocess.run(["git", "-C", src, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
with open(os.path.join(DEST, "VERSION"), "w") as f:
    f.write(f"Windmill {head} — spine generated {spine['generatedAt']}, benchmark list v{spine['benchmarkList']['version']}, "
            f"{sum(1 for v in spine['days'].values() if 'holiday' not in v)} school days\n")
print(open(os.path.join(DEST, "VERSION")).read().strip())
