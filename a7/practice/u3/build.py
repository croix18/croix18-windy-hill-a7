"""Assemble the practice test page: the test page's sheet styles + practice styles, the engine, the page script."""
import os
D = os.path.dirname(os.path.abspath(__file__))
r = lambda f: open(os.path.join(D, f), encoding="utf-8").read()
body = f"""<title>Unit 3 Practice Test</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap">
<style>{r('base.css')}{r('extra.css')}</style>
<div class="watch" role="region" aria-label="Stopwatch and score"><div class="in">
  <div class="time" id="time" aria-live="off">0:00</div>
  <div class="score" id="score"></div>
  <div class="btns"><button type="button" class="go" id="bStart">Start</button><button type="button" id="bPause" hidden>Pause</button><button type="button" id="bFinish">Finish</button></div>
  <div class="confirm" id="confirm" hidden></div>
</div><div class="bar"><i id="prog"></i></div></div>
<div class="result" id="result" hidden></div>
<main class="sheet">
  <div class="head"><div><div class="eyebrow">Grade 7 Accelerated &nbsp;·&nbsp; Unit 3 &nbsp;·&nbsp; Practice</div><h1>Exponents and Scientific Notation</h1><div class="total"><span id="total">36 points</span> &nbsp;·&nbsp; set <span id="setno"></span></div></div></div>
  <div class="rules"></div>
  <p class="how">Same kinds of questions as the unit test, with different numbers. Every new set has new numbers.</p>
  <div class="mode" role="group" aria-label="How to practice"><button type="button" data-mode="practice" aria-pressed="true">Check as I go</button><button type="button" data-mode="test" aria-pressed="false">Like the real test</button></div>
  <div class="setrow"><label for="scope">Practice</label><select id="scope" aria-label="What to practice"></select></div>
  <div class="setrow"><label for="setin">Set</label><input type="text" inputmode="numeric" id="setin" aria-label="Set number" autocomplete="off"><button type="button" id="setgo">Go</button><button type="button" class="go" data-new="1">New set</button><button type="button" id="bAgain">Start this set over</button></div>
  <div id="paper"></div>
</main>
<script>{r('engine.js')}</script>
<script>{r('coach.js')}</script>
<script>{r('visual.js')}</script>
<script>{r('walk.js')}</script>
<script>{r('ui.js')}</script>
"""
open(os.path.join(D, "unit-3-practice-test.html"), "w", encoding="utf-8").write(body)
open(os.path.join(D, "preview.html"), "w", encoding="utf-8").write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + body + "</body></html>")
print(len(body), "bytes")
