(function(){
'use strict';
var E = window.Practice, VER = 'v2', PRE = 'a7u3prac.' + VER + '.';
var $ = function(id){ return document.getElementById(id); };
var LET = 'ABCDE';
function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function load(k){ try { return JSON.parse(localStorage.getItem(PRE + k) || 'null'); } catch(e){ return null; } }
function store(k, v){ try { localStorage.setItem(PRE + k, JSON.stringify(v)); } catch(e){} }
function drop(k){ try { localStorage.removeItem(PRE + k); } catch(e){} }
function randomSeed(){ var a = new Uint32Array(1); try { crypto.getRandomValues(a); } catch(e){ a[0] = Math.floor(Math.random()*4294967296); } return 1 + (a[0] % 99999); }

/* ------------------------------------------------ which set */
function seedFromHash(){ var m = /set-?(\d{1,5})/i.exec(location.hash || ''); return m && +m[1] >= 1 ? +m[1] : null; }
var seed = seedFromHash() || load('last') || randomSeed();
var G, ITEMS, S;
function fresh(mode){ return {mode: mode || 'practice', ans:{}, res:{}, acc:0, startedAt:null, running:false, done:false}; }
function save(){ store('set.' + seed, S); store('last', seed); }

/* ------------------------------------------------ drawing the sheet */
function partHtml(p, id, solo){
  var st = p.text ? p.text.map(function(x){ return typeof x === 'string' ? esc(x) : E.M(x); }).join('') : E.M(p.q) + (p.after ? esc(p.after) : '');
  var line = solo ? '' : '<div class="line"><b class="lab">' + p.label + '.</b><span class="st">' + st + '</span><span class="pt">1 pt</span></div>';
  return '<div class="prt' + (solo ? ' solo' : '') + '" data-id="' + id + '">' + line +
    '<div class="ans">' + (p.kind === 'n' ? '<span class="pre m"><i>n</i> =</span>' : '') +
    '<input type="text" id="a' + id + '" data-kind="' + p.kind + '" aria-label="Answer to ' + id + '" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="done">' +
    '<button type="button" class="chk" data-check="' + id + '">Check</button><span class="pv" aria-hidden="true"></span></div>' +
    '<div class="fb" id="fb' + id + '" aria-live="polite" hidden></div><div class="more" id="mo' + id + '" hidden></div><div class="steps" id="st' + id + '" hidden></div></div>';
}
function render(){
  G = E.generate(seed); ITEMS = [];
  var h = [], qn = 0;
  G.sections.forEach(function(sec, si){
    var pts = sec.items.reduce(function(t, it){ return t + (it.type === 'parts' ? it.parts.length : 1); }, 0);
    h.push('<section class="part"><div class="sechead"><h2>' + (si+1) + '.&nbsp; ' + esc(sec.title) + '</h2><span class="pts">' + pts + ' points</span></div>');
    sec.items.forEach(function(it){
      qn++;
      var q = ['<div class="q" data-q="' + qn + '">'];
      if (it.type === 'parts'){
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + esc(it.stem) + '</span></div>');
        it.parts.forEach(function(p){ var id = qn + p.label; ITEMS.push({id:id, sec:si, type:'text', part:p, item:it}); q.push(partHtml(p, id, false)); });
      } else if (it.type === 'solo'){
        var id = String(qn); ITEMS.push({id:id, sec:si, type:'text', part:it.part, item:it});
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + it.stem + '</span><span class="pt">1 pt</span></div>' + partHtml(it.part, id, true));
      } else {
        var multi = it.type === 'multi', id2 = String(qn);
        ITEMS.push({id:id2, sec:si, type:it.type, item:it});
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + it.stem + '</span><span class="pt">1 pt</span></div>');
        q.push('<div class="choices" role="' + (multi ? 'group' : 'radiogroup') + '" data-id="' + id2 + '">');
        it.opts.forEach(function(o, k){
          q.push('<label class="ch" id="ch' + id2 + LET[k] + '"><input type="' + (multi ? 'checkbox' : 'radio') + '" name="q' + id2 + '" value="' + k + '"><span class="box' + (multi ? ' sq' : '') + '"></span><span class="cl">' + LET[k] + '.</span><span class="cv">' + E.M(o) + '</span></label>');
        });
        q.push('</div><div class="ckrow"><button type="button" class="chk" data-check="' + id2 + '">Check</button></div>' +
          '<div class="fb" id="fb' + id2 + '" aria-live="polite" hidden></div><div class="more" id="mo' + id2 + '" hidden></div><div class="steps" id="st' + id2 + '" hidden></div>');
      }
      q.push('</div>'); h.push(q.join(''));
    });
    h.push('</section>');
  });
  $('paper').innerHTML = h.join('');
  $('setno').textContent = seed;
  $('setin').value = seed;
}

/* ------------------------------------------------ marking and coaching */
var C = window.Coach;
function byId(id){ for (var i = 0; i < ITEMS.length; i++) if (ITEMS[i].id === id) return ITEMS[i]; return null; }
function answered(it){ var a = S.ans[it.id]; return it.type === 'multi' ? !!(a && a.length) : a != null && String(a).trim() !== ''; }
function judge(it, triesSoFar){            /* → {v, what[], rule, step} without touching the state */
  var a = S.ans[it.id];
  if (!answered(it)) return {v:'blank', what:[]};
  try {
    if (it.type === 'text') return C.feedback(it.part, a);
    if (it.type === 'mc') return C.mcFeedback(it.item, +a);
    return C.selectFeedback(it.item, a, (triesSoFar || 0) + 1);
  } catch(e){ return {v:'unread', what:['I can’t read that. Type a power with ^ and a fraction with /.']}; }
}
function res(it){ return S.res[it.id] || (S.res[it.id] = {tries:0, first:null, v:null, shown:false, hinted:false, steps:0, fb:null}); }
function record(it, f){                    /* a counted attempt */
  var R = res(it);
  if (R.v === 'right') return R;
  R.tries++; R.v = f.v; R.fb = {what: f.what || [], rule: f.rule || '', step: f.step == null ? null : f.step};
  if (R.first === null) R.first = (f.v === 'right') && !R.hinted;
  return R;
}
function check(id){
  var it = byId(id); if (!it) return;
  var R0 = S.res[it.id], f = judge(it, R0 ? R0.tries : 0);
  if (f.v === 'blank' || f.v === 'unread'){ flash(it, f); return; }      /* a typo is not an attempt */
  if (!S.running && !S.done) start();
  record(it, f); save(); paintItem(it); paintScore();
}
var TAG = {right:'<span class="tag ok">✓ Correct</span>', form:'<span class="tag fm">Almost</span>', wrong:'<span class="tag no">✗ Not yet</span>', unread:'<span class="tag fm">Not counted yet</span>'};
function flash(it, f){
  var fb = $('fb' + it.id);
  fb.innerHTML = f.v === 'blank' ? '<div class="fbx"><p>' + (it.type === 'text' ? 'Type an answer first.' : 'Pick an answer first.') + '</p></div>'
    : TAG.unread + '<div class="fbx"><p>' + (f.what[0] || '') + '</p></div>';
  fb.hidden = false;
}
function cardHtml(it, R){
  var v = R.v, fb = R.fb || {what:[]}, h = TAG[v] || '';
  if (v === 'right'){
    var note = R.first ? '' : R.shown ? 'after seeing the steps' : R.hinted && R.tries === 1 ? 'with a hint' : 'on try ' + R.tries;
    return h + (note ? '<span class="msg">' + note + '</span>' : '');
  }
  var w = fb.what || [];
  var body = w.length > 1 ? '<ul>' + w.map(function(x){ return '<li>' + x + '</li>'; }).join('') + '</ul>' : (w.length ? '<p>' + w[0] + '</p>' : '');
  if (v === 'wrong' && fb.rule) body += '<p class="rule"><b>Next time:</b> ' + fb.rule + '</p>';
  if (v === 'wrong' && fb.step != null && R.steps <= fb.step) body += '<p class="where">Tap <b>Show me how</b> to see the step where it went off.</p>';
  return h + '<div class="fbx">' + body + '</div>';
}
function keyHtml(it){
  if (it.type === 'mc') return '<b>' + LET[it.item.correct] + '.</b> ' + E.M(it.item.opts[it.item.correct]);
  if (it.type === 'multi') return it.item.correct.map(function(k){ return '<b>' + LET[k] + '.</b> ' + E.M(it.item.opts[k]); }).join('&nbsp;&nbsp; ');
  var p = it.part;
  return (p.kind === 'n' ? '<span class="m"><i>n</i> = </span>' : '') + E.M(p.shownAns || p.ans) + (p.tail ? esc(p.tail) : '');
}
function solOf(it){
  try { return it.type === 'text' ? C.solution(it.part) : C.mcSolution(it.item); } catch(e){ return null; }
}
function stepsHtml(it, R){
  var sol = solOf(it), n = sol ? sol.length : 0, shown = Math.min(R.steps || 0, n);
  if (!sol){                                                     /* fallback: the plain steps */
    var src = it.type === 'text' ? it.part.steps : it.item.steps || [];
    return '<ol class="sol">' + src.map(function(s){ return '<li><div class="say">' + (typeof s === 'string' ? s : '') + '</div></li>'; }).join('') + '</ol><div class="key"><span class="kl">Answer</span><span class="kv">' + keyHtml(it) + '</span></div>';
  }
  var q = it.type === 'text' ? it.part.q : it.item.q, eq = it.type === 'text' && it.part.fam === 'solveN';
  var off = (R.v !== 'right' && R.fb && R.fb.step != null) ? R.fb.step : -1;
  var h = q && it.type !== 'multi' ? '<div class="solhead"><span class="kl">Start</span> ' + E.M(q) + '</div>' : '';
  h += '<ol class="sol">' + sol.slice(0, shown).map(function(s, i){
    return '<li class="' + (i === off ? 'off' : '') + '"><div class="say">' + s.say + '</div>' +
      (s.ex ? '<div class="ex">' + (eq ? '' : '<span class="m">= </span>') + E.M(s.ex) + '</div>' : '') +
      (i === off ? '<div class="offnote">⟵ This is the step where your answer went off.</div>' : '') + '</li>';
  }).join('') + '</ol>';
  if (shown >= n) h += '<div class="key"><span class="kl">Answer</span><span class="kv">' + keyHtml(it) + '</span></div>';
  return h;
}
function paintItem(it){
  var R = S.res[it.id], host = it.type === 'text' ? document.querySelector('.prt[data-id="' + it.id + '"]') : document.querySelector('.q[data-q="' + it.id + '"]');
  var testHidden = S.mode === 'test' && !S.done;
  ['is-right','is-wrong','is-form'].forEach(function(c){ host.classList.remove(c); });
  var fb = $('fb' + it.id), mo = $('mo' + it.id), st = $('st' + it.id);
  if (testHidden){ fb.hidden = true; mo.hidden = true; st.hidden = true; paintChoices(it, null); return; }
  var sol = solOf(it), n = sol ? sol.length : 1;
  R = R || {tries:0, v:null, steps:0};
  if (R.v) host.classList.add(R.v === 'right' ? 'is-right' : R.v === 'form' ? 'is-form' : 'is-wrong');
  if (R.v){ fb.innerHTML = cardHtml(it, R); fb.hidden = false; } else fb.hidden = true;
  var b = [];
  var all = (R.steps || 0) >= n;
  if (R.v === 'right'){ if (!all) b.push('<button type="button" data-all="' + it.id + '">See the steps</button>'); }
  else if (!all){
    b.push('<button type="button" data-hint="' + it.id + '">' + ((R.steps || 0) === 0 ? 'Hint' : 'Next step') + ' <span class="cnt">' + Math.min((R.steps || 0) + 1, n) + ' of ' + n + '</span></button>');
    if (R.tries > 0 || S.done) b.push('<button type="button" data-all="' + it.id + '">Show me how</button>');
  }
  mo.innerHTML = b.join(''); mo.hidden = !b.length;
  st.hidden = !(R.steps > 0); if (R.steps > 0) st.innerHTML = stepsHtml(it, R);
  paintChoices(it, R.v ? R : null);
  var input = $('a' + it.id); if (input) input.readOnly = R.v === 'right';
  var btn = host.querySelector('[data-check="' + it.id + '"]'); if (btn) btn.disabled = R.v === 'right';
  if (it.type !== 'text') Array.prototype.forEach.call(host.querySelectorAll('.ch input'), function(x){ x.disabled = R.v === 'right'; });
}
function paintChoices(it, R){
  if (it.type === 'text') return;
  it.item.opts.forEach(function(o, k){
    var ch = $('ch' + it.id + LET[k]); ch.classList.remove('picked-no','is-key');
    if (!R) return;
    var sol = solOf(it), all = sol && R.steps >= sol.length;
    var picked = it.type === 'mc' ? String(S.ans[it.id]) === String(k) : (S.ans[it.id] || []).map(Number).indexOf(k) >= 0;
    var isKey = it.type === 'mc' ? k === it.item.correct : it.item.correct.indexOf(k) >= 0;
    if (R.v === 'right' || all){ if (isKey) ch.classList.add('is-key'); }
    else if (picked && it.type === 'mc' && R.v === 'wrong') ch.classList.add('picked-no');
  });
}
document.addEventListener('click', function(e){
  var b = e.target.closest && e.target.closest('[data-check]'); if (b){ check(b.dataset.check); return; }
  var h = e.target.closest && e.target.closest('[data-hint]');
  if (h){ var it = byId(h.dataset.hint), R = res(it);
    if (R.tries === 0 && !S.done) R.hinted = true;               /* a hint before the first check: that question can't count as first try */
    R.steps = (R.steps || 0) + 1;
    var sol = solOf(it); if (sol && R.steps >= sol.length && R.v !== 'right'){ R.shown = true; if (R.first === null) R.first = false; }
    if (!S.running && !S.done) start();
    save(); paintItem(it); paintScore(); return; }
  var a = e.target.closest && e.target.closest('[data-all]');
  if (a){ var it2 = byId(a.dataset.all), R2 = res(it2), sol2 = solOf(it2);
    R2.steps = sol2 ? sol2.length : 1;
    if (R2.v !== 'right'){ R2.shown = true; if (R2.first === null) R2.first = false; }
    save(); paintItem(it2); paintScore(); }
});

/* ------------------------------------------------ typing */
var keys = document.createElement('div'); keys.className = 'keys'; keys.hidden = true;
['^','/','×','−','(',')'].forEach(function(k){ var b = document.createElement('button'); b.type = 'button'; b.textContent = k; b.setAttribute('aria-label', 'Insert ' + k); b.dataset.k = k; keys.appendChild(b); });
keys.addEventListener('pointerdown', function(e){ if (e.target.dataset.k) e.preventDefault(); });
keys.addEventListener('click', function(e){
  var k = e.target.dataset.k, el = keys.target; if (!k || !el || el.readOnly) return;
  var kind = el.dataset.kind, sciish = kind === 'sci' || kind === 'std' || kind === 'times';
  var ins = k === '×' ? (sciish ? ' x ' : '*') : k === '−' ? '-' : k, a = el.selectionStart, b = el.selectionEnd;
  if (a == null){ a = b = el.value.length; }
  el.value = el.value.slice(0,a) + ins + el.value.slice(b); el.focus(); try { el.setSelectionRange(a+ins.length, a+ins.length); } catch(x){}
  el.dispatchEvent(new Event('input', {bubbles:true}));
});
function pretty(s, kind){
  var h = esc(s).replace(/-/g, '−');
  h = h.replace(/\^\(?(−?[0-9a-z]+)\)?/gi, '<sup>$1</sup>');
  if (kind === 'sci' || kind === 'std' || kind === 'times') h = h.replace(/([0-9])\s*[x*]\s*(?=10)/gi, '$1 × ');
  return h.replace(/\*/g, '·');
}
function setPreview(el){ var pv = el.parentNode.querySelector('.pv'); if (!pv) return; var p = pretty(el.value, el.dataset.kind); pv.innerHTML = (p !== esc(el.value)) ? p : ''; }
document.addEventListener('focusin', function(e){
  if (e.target.matches && e.target.matches('#paper input[type=text]') && !e.target.readOnly){ keys.target = e.target; e.target.parentNode.appendChild(keys); keys.hidden = false; }
  else if (!(e.target.closest && e.target.closest('.keys'))) keys.hidden = true;
});
document.addEventListener('input', function(e){
  var t = e.target; if (!t.id || t.id.charAt(0) !== 'a' || !t.closest('#paper')) return;
  if (!S.running && !S.done) start();
  S.ans[t.id.slice(1)] = t.value; setPreview(t);
  save(); paintProgress();
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Enter' && e.target.matches && e.target.matches('#paper input[type=text]')){ e.preventDefault(); if (S.mode === 'practice' || S.done) check(e.target.id.slice(1)); }
});
document.addEventListener('change', function(e){
  var t = e.target; if (!t.name || t.name.charAt(0) !== 'q' || !t.closest('#paper')) return;
  if (!S.running && !S.done) start();
  var id = t.name.slice(1);
  if (t.type === 'radio') S.ans[id] = t.value;
  else S.ans[id] = Array.prototype.map.call(document.querySelectorAll('input[name="q' + id + '"]:checked'), function(x){ return x.value; });
  save(); paintProgress();
});

/* ------------------------------------------------ the clock and the score */
function now(){ return Date.now(); }
function elapsed(){ return S.acc + (S.running && S.startedAt ? (now() - S.startedAt)/1000 : 0); }
function fmt(s){ s = Math.max(0, Math.round(s)); var m = Math.floor(s/60), r = s%60; return m + ':' + (r<10?'0':'') + r; }
function start(){ if (S.running || S.done) return; S.running = true; S.startedAt = now(); save(); paintBar(); }
function pause(){ if (!S.running) return; S.acc = elapsed(); S.running = false; S.startedAt = null; save(); paintBar(); }
function tally(){
  var first = 0, done = 0, bySec = G.sections.map(function(){ return {got:0, of:0}; });
  ITEMS.forEach(function(it){ var R = S.res[it.id]; bySec[it.sec].of++; if (R && R.first === true){ first++; bySec[it.sec].got++; } if (R && R.v === 'right') done++; });
  return {first:first, done:done, bySec:bySec};
}
function paintProgress(){ var n = ITEMS.filter(answered).length; $('prog').style.width = (100*n/ITEMS.length) + '%'; return n; }
function paintScore(){
  var t = tally(), sc = $('score');
  if (S.mode === 'test' && !S.done) sc.innerHTML = '<b>' + ITEMS.filter(answered).length + ' of ' + ITEMS.length + '</b> answered · marked when you finish';
  else sc.innerHTML = 'First try <b>' + t.first + ' / ' + ITEMS.length + '</b> · solved <b>' + t.done + '</b>';
  paintResult(t);
}
function paintBar(){
  $('time').textContent = fmt(elapsed());
  $('bStart').hidden = S.done || S.running; $('bStart').textContent = elapsed() > 0 ? 'Resume' : 'Start';
  $('bPause').hidden = S.done || !S.running;
  $('bFinish').hidden = S.done;
  $('bFinish').textContent = S.mode === 'test' ? 'Finish & mark' : 'Finish';
  document.body.classList.toggle('hidechk', S.mode === 'test' && !S.done);
  Array.prototype.forEach.call(document.querySelectorAll('.mode button'), function(b){ b.setAttribute('aria-pressed', String(b.dataset.mode === S.mode)); });
}
function paintResult(t){
  var box = $('result');
  if (!S.done){ box.hidden = true; return; }
  var rows = G.sections.map(function(s, k){ return '<tr><td>' + (k+1) + '. ' + esc(s.title) + '</td><td class="r">' + t.bySec[k].got + ' / ' + t.bySec[k].of + '</td></tr>'; }).join('');
  var weak = G.sections.map(function(s, k){ return [s.title, t.bySec[k].got / t.bySec[k].of]; }).filter(function(x){ return x[1] < 0.8; }).map(function(x){ return x[0]; });
  box.innerHTML = '<h2>Set ' + seed + ' · ' + (S.mode === 'test' ? 'test style' : 'checked as you went') + '</h2>' +
    '<div class="big"><div><b>' + t.first + '<small> / ' + ITEMS.length + '</small></b><span>right on the first try</span></div><div><b>' + fmt(S.acc) + '</b><span>time on the clock</span></div></div>' +
    '<div class="tw"><table><thead><tr><th>Part</th><th class="r">First try</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
    '<p class="note">' + (weak.length ? 'Practice more: ' + weak.map(esc).join(', ') + '. ' : 'Every part at 80% or better. ') +
    'Fix the ones that aren’t right yet — tap <b>Show me how</b> for the steps — or start a new set with new numbers.</p>' +
    '<div class="btns"><button type="button" class="go" data-new="1">New set</button></div>';
  box.hidden = false;
}
function finish(){
  if (S.running) S.acc = elapsed(); S.running = false; S.startedAt = null; S.done = true;
  if (S.mode === 'test'){ ITEMS.forEach(function(it){ var R = res(it), f = judge(it, R.tries);
      if (f.v === 'blank' || f.v === 'unread'){ R.first = false; R.v = 'wrong'; R.tries = 1; R.fb = {what: [f.v === 'blank' ? 'Left blank.' : (f.what[0] || 'Could not read the answer.')], rule: '', step: null}; }
      else record(it, f); }); }
  else ITEMS.forEach(function(it){ var R = res(it); if (R.first === null) R.first = false; });
  save(); paintAll(); window.scrollTo(0, 0);
}

/* ------------------------------------------------ buttons */
function ask(text, yes, fn){
  var c = $('confirm'); c.hidden = false;
  c.innerHTML = '<span>' + text + '</span><button type="button" class="go" id="cy">' + yes + '</button><button type="button" id="cn">Cancel</button>';
  $('cy').onclick = function(){ c.hidden = true; fn(); }; $('cn').onclick = function(){ c.hidden = true; };
}
function started(){ return elapsed() > 0 || ITEMS.some(answered) || Object.keys(S.res).length > 0; }
function openSet(n, mode){
  if (S) pause(); seed = n; var saved = load('set.' + seed);
  S = saved && saved.res ? saved : fresh(mode || (S && S.mode) || 'practice');
  if (saved && mode && saved.mode !== mode && !Object.keys(saved.res).length && !saved.acc){ S.mode = mode; }
  S.running = false; S.startedAt = null;
  try { history.replaceState(null, '', '#set-' + seed); } catch(e){ location.hash = 'set-' + seed; }
  render(); restore(); save(); paintAll(); window.scrollTo(0, 0);
}
function restore(){
  ITEMS.forEach(function(it){
    var a = S.ans[it.id]; if (a == null) return;
    if (it.type === 'text'){ var el = $('a' + it.id); el.value = a; setPreview(el); }
    else (it.type === 'mc' ? [a] : a).forEach(function(v){ var x = document.querySelector('input[name="q' + it.id + '"][value="' + v + '"]'); if (x) x.checked = true; });
  });
}
function paintAll(){ paintBar(); paintProgress(); ITEMS.forEach(paintItem); paintScore(); }
$('bStart').addEventListener('click', start);
$('bPause').addEventListener('click', pause);
$('bFinish').addEventListener('click', function(){
  var left = ITEMS.length - ITEMS.filter(answered).length;
  ask((left ? left + ' of ' + ITEMS.length + ' still blank. ' : '') + (S.mode === 'test' ? 'Stop the clock and mark everything?' : 'Stop the clock and see your score?'), 'Finish', finish);
});
document.addEventListener('click', function(e){
  var n = e.target.closest && e.target.closest('[data-new]'); if (!n) return;
  if (started() && !S.done) ask('Leave this set? It stays saved on this device under set ' + seed + '.', 'New set', function(){ openSet(randomSeed()); });
  else openSet(randomSeed());
});
Array.prototype.forEach.call(document.querySelectorAll('.mode button'), function(b){
  b.addEventListener('click', function(){
    var m = b.dataset.mode; if (m === S.mode) return;
    var go = function(){ drop('set.' + seed); S = fresh(m); render(); save(); paintAll(); };
    if (started()) ask('Switching starts set ' + seed + ' over. Your answers will be cleared.', 'Switch', go); else go();
  });
});
$('setgo').addEventListener('click', function(){ var v = Math.floor(+$('setin').value); if (v >= 1 && v <= 99999) openSet(v); else { $('setin').value = seed; } });
$('setin').addEventListener('keydown', function(e){ if (e.key === 'Enter'){ e.preventDefault(); $('setgo').click(); } });
$('bAgain').addEventListener('click', function(){ ask('Clear your answers to set ' + seed + ' and start it again?', 'Start over', function(){ var m = S.mode; drop('set.' + seed); S = fresh(m); render(); save(); paintAll(); window.scrollTo(0,0); }); });
window.addEventListener('hashchange', function(){ var h = seedFromHash(); if (h && h !== seed) openSet(h); });
setInterval(function(){ if (S && S.running) $('time').textContent = fmt(elapsed()); }, 500);
window.addEventListener('pagehide', function(){ if (S.running){ S.acc = elapsed(); S.startedAt = now(); save(); } });

openSet(seed);
})();
