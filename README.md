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

    a7/packages/     the shipped teaching packages, exactly as delivered (20 Sept: as re-cut to
                     the 14 Sept model — nine-question rounds, IXL last, no worksheets, no grey
                     bars, no speaker notes on slides)
    a7/reference/    the rulebook (HOUSE STYLE.md) and the standing reference documents
    a7/build/        generators, figure libraries and figure indexes    ← being rebuilt
    tools/           the check suite and finish() choke point            ← being rebuilt

## The rulebook is the master

`a7/reference/HOUSE STYLE.md` is shared with the on-level (M7) course and exchanged against a
stated base — see the `<!-- exchange:base … -->` line at its top. Rule 0, above everything:
nothing that touches students goes out mathematically unsound.

## Pushing

`tools/push.sh "message"` commits everything and pushes, then checks the remote head against
the local one — trust that check, not git's message. The token lives in `.github-token`
(git-ignored). Why the script exists: `a7/reference/GITHUB FROM A SESSION.md`. Commits are
authored as Croix's GitHub no-reply address because his account rejects pushes that expose his
email. Remote: github.com/croix18/croix18-windy-hill-a7.
