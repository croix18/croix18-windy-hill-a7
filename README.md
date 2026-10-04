# Windy Hill Math — Grade 7 Accelerated (A7)

Course 1205050 · Grade 8 FAST · Windy Hill Middle School, Lake County FL.
Croix Shaffer's materials. Built by Claude; every value re-derived independently before it ships.

## Why this repository exists

On 20 September 2026 the container that held the build system was reclaimed. The shipped
packages survived because they had been sent out; the **85 generators, 3,663 figure images,
24-check suite and the re-derivation ledger did not**, because they had never left the
container. That was a week of work and it was avoidable.

**The rule from here on: nothing exists until it is committed.** A build that is not pushed did
not happen.

## Layout

    a7/packages/     what ships: one folder per unit, laid out by lesson — All Slides/,
                     Lessons/<N.NN>/ (number only; its keys in Keys/), Review/, Assessment/, Handouts/,
                     Reference/ — every file named course, number, title, what it is
                     ("A7 3.08 Writing Large Numbers in Scientific Notation - Slides.pptx";
                     ruling 34, 4 Oct 2026). Units 3 on are written by the build; Units 1-2
                     predate it and were renamed, never rebuilt. zips/ is git-ignored.
    a7/reference/    the rulebook (HOUSE STYLE.md), the scope and sequence, the IXL due dates,
                     each unit's audit and question-bank file, the master sheet, and
                     "A7 Rename List 2026-10-04.csv" (every old file name and its new one)
    a7/for Croix/    documents made for him outside the unit packages
    a7/build/        the build system (Python): specs per unit in a7/build/<unit>/, the
                     course profile (course.py), the installer — and the SHARED BUILD KIT
                     (lib/, checks.py, gates.py, the drivers, SPEC SCHEMA.md), which is
                     published from croix18/Windmill (kit/), vendored here and never edited
                     here (KIT.sha256). The on-level course is built by the same kit.
                     START WITH a7/build/BUILDING A UNIT.md — the whole procedure.
    tools/           setup_env.sh (fresh session), push.sh, check.sh (run before every push
                     and by CI), vendor_windmill.py, the scope calendar, PDF helpers,
                     master_sheet.py and its check, zip_package.py (zips for Units 1-2;
                     a built unit is zipped by its install), legacy/ (the 4 Oct renaming)

## Building the next unit

1. `bash tools/setup_env.sh` in a fresh session, then `cd a7/build && python3 build_all.py u3` (the PDFs are git-ignored; this regenerates them and proves the toolchain).
2. Follow `a7/build/BUILDING A UNIT.md` in order: intake → audit (sent first) → one lesson at a
   time, each built, checked, viewed and pushed → unit documents → manifest → install → report.
3. Unit 3 (`a7/build/u3/`) is the reference implementation; copy its specs, never start blank.

## The rulebook is the master

`a7/reference/HOUSE STYLE.md` is shared with the on-level (M7) course and exchanged against a
stated base — see the `<!-- exchange:base … -->` line at its top. Rule 0, above everything:
nothing that touches students goes out mathematically unsound.

## Pushing

`tools/push.sh "message"` runs `tools/check.sh` (every build gate over every unit's specs, the kit
against its manifest, the IXL due-date sheet, a package for every unit), commits everything and
pushes, then checks the remote head against
the local one — trust that check, not git's message. The token lives in `.github-token`
(git-ignored). Why the script exists: `a7/reference/GITHUB FROM A SESSION.md`. Commits are
authored as Croix's GitHub no-reply address because his account rejects pushes that expose his
email. Remote: github.com/croix18/croix18-windy-hill-a7.
