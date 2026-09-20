# Pushing to GitHub from a Claude session — what actually works

*From the M7 session, 20 September 2026. Written for the A7 session after it hit the same
walls. Three things look like a bad token and are not.*

## 1. The sandbox proxy answers git's first request with 403, not 401

Git sends its first request **without** credentials and expects a 401 challenge before it
offers them. The proxy in these sessions returns 403 to that unauthenticated request, so git
gives up — "could not read Username for 'https://github.com': terminal prompts disabled", or a
bare `error: 403` — and never sends the token.

The fix is to send the token preemptively on every request, as a **Basic** header (not Bearer;
GitHub's git endpoints want Basic):

```sh
T='<token>'
B=$(printf 'x-access-token:%s' "$T" | base64 -w0)
git -c "http.https://github.com/.extraheader=Authorization: Basic $B" push origin main
```

Same trick for `ls-remote` and `fetch`. Putting the token in the remote URL does **not** work
here, for the same reason.

The GitHub **API** (`api.github.com/repos/...`) is blocked per repository by the proxy no
matter what token you hold — don't diagnose with it. `api.github.com/user` returns 200 and tells
you nothing about repo access. Diagnose with the git endpoint itself:

```sh
curl -s -o /dev/null -w "%{http_code}\n" -u "x-access-token:$T" \
  "https://github.com/<owner>/<repo>.git/info/refs?service=git-receive-pack"
```

- `200` — the token can push.
- `401` — the token cannot reach that repo: wrong repository selected on the fine-grained
  token, Contents not set to *read and write*, or the token was revoked.

## 2. Croix's account blocks pushes that expose his email

A commit authored with `croix.shaffer@gmail.com` is rejected: *push declined due to email
privacy restrictions*. Author commits as

```
Croix Shaffer <268190892+croix18@users.noreply.github.com>
```

(his GitHub no-reply address), or — what the stop-hook in these sessions asks for —
`Claude <noreply@anthropic.com>` with the `Co-Authored-By` trailer. Either pushes.

```sh
git config user.name Claude
git config user.email noreply@anthropic.com
git commit --amend --no-edit --reset-author      # for a commit already made
```

## 3. The push script's error message can lie

My `tools/push.sh` printed the "could not read Username" line while the push had in fact
succeeded on git's second request. After any push, check the remote directly rather than
trusting the message:

```sh
git -c "http.https://github.com/.extraheader=Authorization: Basic $B" ls-remote origin main
git log -1 --format=%H
```

The two hashes should match.

## The setup that works

- Keep the token in a git-ignored file — `.github-token`, `chmod 600` — never in the repo,
  never in the remote URL. Add `.github-token` to `.gitignore` before the first commit.
- A `tools/push.sh` that reads it, does `git add -A && git commit`, then pushes with the header
  above. The working one is in the M7 repo: copy it.
- Fine-grained token: **Only select repositories** → the one repo; **Contents: Read and write**;
  nothing else is needed.
- If Croix revokes a token after a push (he did once, as suggested), the symptom is `401` on
  the receive-pack probe while `/user` still returns 200. Ask for a new one; don't debug.

## Where M7 is

`github.com/croix18/windy-hill-m7`. `README.md` is the start-here; `Reference/TRUTH - Grade 7
Benchmarks.md` is the document of truth and `Reference/HOUSE STYLE.md` the rulebook. Ruling 3
stands — M7 owns the rulebook master; take the current copy from there rather than an older one.
