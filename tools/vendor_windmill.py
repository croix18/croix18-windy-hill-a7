#!/usr/bin/env python3
"""Bring Windmill's shared pieces into this repository's build folder: the build kit (lib/,
checks.py, the drivers and tools, assets/) with its manifest, and the room (reader, benchmark
list, spine) for the console.

    python3 tools/vendor_windmill.py [path/to/Windmill]     (default: ../Windmill or ../windmill)

The copying is done by Windmill's own tools/vendor_into.py, so both courses vendor the same way.
Nothing it writes is edited here: change it in Windmill, then vendor again. checks.py's `kitcheck`
refuses a copy that differs from the manifest. BUILDING A UNIT §5b.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, ".."))
BUILD = os.path.join(ROOT, "a7", "build")
cands = [sys.argv[1]] if len(sys.argv) > 1 else [os.path.join(ROOT, "..", "Windmill"), os.path.join(ROOT, "..", "windmill")]
src = next((os.path.abspath(c) for c in cands if os.path.isdir(c)), None)
if not src:
    sys.exit("vendor_windmill: no Windmill checkout found; pass its path")
sys.exit(subprocess.run([sys.executable, os.path.join(src, "tools", "vendor_into.py"), BUILD]).returncode)
