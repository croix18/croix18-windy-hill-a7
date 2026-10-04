#!/usr/bin/env bash
# What can be checked without building. tools/push.sh runs this before every push; CI runs it on
# every push. The full suite (eighteen checks over rendered pages) needs LibreOffice and a browser
# and runs in `a7/build/build_all.py uN` — a unit ships only at `checks: 0 findings`.
set -euo pipefail
cd "$(dirname "$0")/.."
fail() { echo "CHECK FAILED: $*" >&2; exit 1; }

echo "== secrets"
if git grep -nIE --untracked 'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}' -- . ':!tools/check.sh'; then
  fail "a token is in the tree"; fi
git check-ignore -q .github-token || fail ".github-token is not git-ignored"

echo "== the build kit against its manifest, and every gate over every unit's specs"
python3 a7/build/gates.py

echo "== the scope and the IXL due-date sheet regenerate to what is committed (the sequence, the calendar and the as-run log)"
cp "a7/reference/A7 IXL Due Dates 2026-27.md" /tmp/a7_ixl.$$ ; cp "a7/reference/A7 Scope and Sequence 2026-27.md" /tmp/a7_scope.$$
python3 tools/scope_calendar.py >/dev/null 2>/tmp/a7_scope_err.$$ || { cat /tmp/a7_scope_err.$$; fail "tools/scope_calendar.py does not run"; }
cmp -s /tmp/a7_ixl.$$ "a7/reference/A7 IXL Due Dates 2026-27.md" || fail "tools/scope_calendar.py no longer writes the committed IXL due-date sheet"
cmp -s /tmp/a7_scope.$$ "a7/reference/A7 Scope and Sequence 2026-27.md" || fail "tools/scope_calendar.py no longer writes the committed scope and sequence"
rm -f /tmp/a7_ixl.$$ /tmp/a7_scope.$$ /tmp/a7_scope_err.$$

echo "== every unit with specs has an installed package"
for u in a7/build/u[0-9]*; do
  n=${u##*/u}
  ls -d "a7/packages/A7 Unit $n - "*/ >/dev/null 2>&1 || fail "unit $n has specs and no package in a7/packages (build_all.py u$n --install)"
  [ -f "$(ls -d "a7/packages/A7 Unit $n - "*/ | head -1)00 - START HERE.md" ] || fail "unit $n's package has no START HERE"
done
echo "== the master sheet: every link reaches a file this commit holds, none longer than 255 characters"
if python3 -c "import openpyxl, pymupdf" 2>/dev/null; then
  python3 tools/check_master_sheet.py > /tmp/a7_ms.$$ 2>&1 || { tail -n 20 /tmp/a7_ms.$$; rm -f /tmp/a7_ms.$$; fail "the master sheet (python3 tools/master_sheet.py, recalculate, then tools/check_master_sheet.py)"; }
  tail -n 2 /tmp/a7_ms.$$; rm -f /tmp/a7_ms.$$
else
  echo "   skipped: openpyxl and pymupdf are not installed here"
fi
echo "all checks passed"
