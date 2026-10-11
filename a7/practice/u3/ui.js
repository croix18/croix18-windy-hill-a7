(function(){
'use strict';
var E = window.Practice, C = window.Coach, VZ = window.Visual, VER = 'v3',   /* "Help me solve this" was taken out on 11 Oct at Croix's word; its code stays but no button opens it */ PRE = 'a7u3prac.' + VER + '.';
var $ = function(id){ return document.getElementById(id); };
var LET = 'ABCDE';
function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function load(k){ try { return JSON.parse(localStorage.getItem(PRE + k) || 'null'); } catch(e){ return null; } }
function store(k, v){ try { localStorage.setItem(PRE + k, JSON.stringify(v)); } catch(e){} }
function drop(k){ try { localStorage.removeItem(PRE + k); } catch(e){} }
function randomSeed(){ var a = new Uint32Array(1); try { crypto.getRandomValues(a); } catch(e){ a[0] = Math.floor(Math.random()*4294967296); } return 1 + (a[0] % 99999); }

/* ------------------------------------------------ which set, which questions */
var SCOPES = { all: 'Whole test', p1: 'Part 1 only: Laws of Exponents', p2: 'Part 2 only: Integer Exponents', p3: 'Part 3 only: Variable Bases', p4: 'Part 4 only: Scientific Notation', miss: 'My misses, with new numbers' };
function fromHash(){ var m = /set-?(\d{1,5})(?:-(p[1-4]|miss))?/i.exec(location.hash || ''); return m && +m[1] >= 1 ? {seed: +m[1], scope: (m[2] || 'all').toLowerCase()} : null; }
var h0 = fromHash(), last = load('last') || {};
var seed = h0 ? h0.seed : (last.seed || randomSeed()), scope = h0 ? h0.scope : (last.scope || 'all');
var G, ITEMS, DS, EX = {}, S;
function key(){ return 'set.' + seed + '.' + scope; }
function fresh(mode){ return {mode: mode || 'practice', ans:{}, res:{}, work:{}, more:{}, acc:0, startedAt:null, running:false, done:false}; }
function save(){ store(key(), S); store('last', {seed: seed, scope: scope}); }
function misses(){ return load('misses') || {}; }
function seed2(n){ return ((n * 7919 + 4243) % 99999) + 1; }                 /* the second round of a one-part set */
function round2(){                                    /* the second round never repeats a round-1 question */
  var mine = {}; G.sections.forEach(function(sec){ sec.items.forEach(function(it){ partsOf(it).forEach(function(p){ try { mine[E.plain(p ? p.q : it.q || it.target)] = 1; } catch(e){} }); }); });
  for (var t = 0; t < 40; t++){
    var g = E.generate(((seed2(seed) + t * 104729) % 99999) + 1), clash = false;
    g.sections.forEach(function(sec){ sec.items.forEach(function(it){ partsOf(it).forEach(function(p){ try { if (mine[E.plain(p ? p.q : it.q || it.target)]) clash = true; } catch(e){} }); }); });
    if (!clash) return g;
  }
  return E.generate(seed2(seed));
}
function posKey(si, ii, pi){ return si + '.' + ii + '.' + pi; }
function partsOf(it){ return it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : [null]; }

/* the questions on the page: sections of {item, parts subset, pos} */
function build(){
  G = E.generate(seed);
  var rounds = scope === 'all' ? [G] : [G, round2()], out = [];
  if (scope === 'all') G.sections.forEach(function(sec, si){ out.push({title: (si + 1) + '.&nbsp; ' + esc(sec.title), items: sec.items.map(function(it, ii){ return {it: it, keep: null, si: si, ii: ii}; })}); });
  else if (scope === 'miss'){
    var pos = S.pos || [];
    rounds.forEach(function(R, r){
      var items = [];
      R.sections.forEach(function(sec, si){ sec.items.forEach(function(it, ii){
        var keep = partsOf(it).map(function(p, pi){ return pos.indexOf(posKey(si, ii, it.type === 'parts' ? pi : -1)) >= 0; });
        if (keep.some(Boolean)) items.push({it: it, keep: it.type === 'parts' ? keep : null, si: si, ii: ii});
      }); });
      if (items.length) out.push({title: 'Your misses — round ' + (r + 1), items: items});
    });
  } else {
    var k = +scope.charAt(1) - 1;
    rounds.forEach(function(R, r){ out.push({title: (k + 1) + '.&nbsp; ' + esc(R.sections[k].title) + ' — round ' + (r + 1), items: R.sections[k].items.map(function(it, ii){ return {it: it, keep: null, si: k, ii: ii}; })}); });
  }
  return out;
}

/* ------------------------------------------------ drawing the sheet */
function partHtml(p, id, solo){
  var st = p.text ? p.text.map(function(x){ return typeof x === 'string' ? esc(x) : E.M(x); }).join('') : E.M(p.q) + (p.after ? esc(p.after) : '');
  var line = solo ? '' : '<div class="line">' + (p.label ? '<b class="lab">' + p.label + '.</b>' : '') + '<span class="st">' + st + '</span>' + (p.label ? '<span class="pt">1 pt</span>' : '') + '</div>';
  return '<div class="prt' + (solo ? ' solo' : '') + '" data-id="' + id + '">' + line +
    '<div class="ans">' + (p.kind === 'n' ? '<span class="pre m"><i>n</i> =</span>' : '') +
    '<input type="text" id="a' + id + '" data-kind="' + p.kind + '" aria-label="Answer to ' + id + '" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="done">' +
    '<button type="button" class="chk" data-check="' + id + '">Check</button><span class="pv" aria-hidden="true"></span></div>' + tailHtml(id, true) + '</div>';
}
function tailHtml(id, text){
  return '<div class="fb" id="fb' + id + '" aria-live="polite" hidden></div><div class="more" id="mo' + id + '" hidden></div>' +
    (text ? '<div class="work" id="wk' + id + '" hidden></div>' : '') + '<div class="steps" id="st' + id + '" hidden></div><div class="again" id="ag' + id + '" hidden></div>';
}
function choicesHtml(it, id){
  var multi = it.type === 'multi', q = ['<div class="choices" role="' + (multi ? 'group' : 'radiogroup') + '" data-id="' + id + '">'];
  it.opts.forEach(function(o, k){
    q.push('<label class="ch" id="ch' + id + LET[k] + '"><input type="' + (multi ? 'checkbox' : 'radio') + '" name="q' + id + '" value="' + k + '"><span class="box' + (multi ? ' sq' : '') + '"></span><span class="cl">' + LET[k] + '.</span><span class="cv">' + E.M(o) + '</span></label>');
  });
  q.push('</div><div class="ckrow"><button type="button" class="chk" data-check="' + id + '">Check</button></div>' + tailHtml(id, false));
  return q.join('');
}
function render(){
  DS = build(); ITEMS = []; EX = {};
  var h = [], qn = 0;
  if (!DS.length) h.push('<p class="how">No misses saved on this device yet. Finish a set first, then come back to practice the ones you missed.</p>');
  DS.forEach(function(sec, di){
    var pts = 0;
    var body = sec.items.map(function(d){
      var it = d.it; qn++;
      var q = ['<div class="q" data-q="' + qn + '">'];
      if (it.type === 'parts'){
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + esc(it.stem) + '</span></div>');
        it.parts.forEach(function(p, pi){ if (d.keep && !d.keep[pi]) return; pts++;
          var id = qn + p.label; ITEMS.push({id:id, sec:di, type:'text', part:p, item:it, pos: posKey(d.si, d.ii, pi), stem: it.stem}); q.push(partHtml(p, id, false)); });
      } else if (it.type === 'solo'){
        pts++; var id = String(qn); ITEMS.push({id:id, sec:di, type:'text', part:it.part, item:it, pos: posKey(d.si, d.ii, -1), stem: it.stem, solo: true});
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + it.stem + '</span><span class="pt">1 pt</span></div>' + partHtml(it.part, id, true));
      } else {
        pts++; var id2 = String(qn);
        ITEMS.push({id:id2, sec:di, type:it.type, item:it, pos: posKey(d.si, d.ii, -1)});
        q.push('<div class="stem"><b class="num">' + qn + '.</b><span class="st">' + it.stem + '</span><span class="pt">1 pt</span></div>' + choicesHtml(it, id2));
      }
      q.push('</div>'); return q.join('');
    }).join('');
    sec.pts = pts;
    h.push('<section class="part"><div class="sechead"><h2>' + sec.title + '</h2><span class="pts">' + pts + ' point' + (pts === 1 ? '' : 's') + '</span></div>' + body + '</section>');
  });
  $('paper').innerHTML = h.join('');
  $('setno').textContent = seed; $('setin').value = seed;
  $('total').textContent = ITEMS.length + ' point' + (ITEMS.length === 1 ? '' : 's');
  paintScopes();
  Object.keys(S.more || {}).forEach(function(id){ var b = ITEMS.filter(function(x){ return x.id === id; })[0]; if (b) mountExtra(b); });
}
function paintScopes(){
  var sc = $('scope'), nm = Object.keys(misses()).length;
  sc.innerHTML = Object.keys(SCOPES).map(function(k){ return '<option value="' + k + '"' + (k === scope ? ' selected' : '') + (k === 'miss' && !nm && scope !== 'miss' ? ' disabled' : '') + '>' + SCOPES[k] + (k === 'miss' ? ' (' + nm + ')' : '') + '</option>'; }).join('');
}

/* ------------------------------------------------ "Try another like this": the same kind of question, new numbers */
function mountExtra(base){
  var M0 = S.more[base.id]; if (!M0) return;
  var g = E.generate(M0.seed), p = base.pos.split('.').map(Number), it = g.sections[p[0]].items[p[1]], id = base.id + 'x' + M0.n, h;
  if (base.type === 'text'){
    var part = it.type === 'parts' ? it.parts[p[2]] : it.part;
    EX[id] = {id:id, type:'text', part:part, item:it, base: base.id, extra: true, pos: base.pos};
    h = '<div class="xq q" data-q="' + id + '"><div class="xhead">Try another like this' + streakHtml(M0) + '</div><div class="stem"><span class="st">' + (it.type === 'parts' ? esc(it.stem) : it.stem) + '</span></div>' +
      (it.type === 'parts' ? partHtml(Object.assign({}, part, {label: ''}), id, false) : partHtml(part, id, true)) + '</div>';
  } else {
    EX[id] = {id:id, type:it.type, item:it, base: base.id, extra: true, pos: base.pos};
    h = '<div class="xq q" data-q="' + id + '"><div class="xhead">Try another like this' + streakHtml(M0) + '</div><div class="stem"><span class="st">' + it.stem + '</span></div>' + choicesHtml(it, id) + '</div>';
  }
  var box = $('ag' + base.id); box.innerHTML = h; box.hidden = false;
  restoreOne(EX[id]); paintItem(EX[id]);
}
function atPos(g, b){ var p = b.pos.split('.').map(Number), it = g.sections[p[0]].items[p[1]]; return b.type === 'text' ? {type:'text', part: it.type === 'parts' ? it.parts[p[2]] : it.part, item: it} : {type: it.type, item: it}; }
function qkey(x){ try { if (x.type === 'text') return E.plain(x.part.q); if (x.type === 'mc') return E.plain(x.item.q) + '|' + x.item.opts.map(E.plain).join(','); return E.plain(x.item.target) + '|' + x.item.opts.map(E.plain).sort().join(','); } catch(e){ return String(Math.random()); } }
function streakHtml(M0){ return M0.streak >= 2 ? ' <span class="streak">✓✓ two in a row — you’ve got this one</span>' : M0.streak === 1 ? ' <span class="streak">✓ one in a row</span>' : ''; }
function another(baseId){
  var M0 = S.more[baseId] || (S.more[baseId] = {n: 0, seed: 0, streak: 0});
  M0.n++; var s, b0 = byId(baseId), was = M0.seed ? qkey(atPos(E.generate(M0.seed), b0)) : null, base = qkey(b0), tries = 0;
  do { s = randomSeed(); tries++; var k = qkey(atPos(E.generate(s), b0)); } while ((s === seed || k === base || k === was) && tries < 60);   /* never the same question again */
  M0.seed = s; save();
  var b = byId(baseId); mountExtra(b); paintItem(b);
  var el = $('ag' + baseId); if (el && el.scrollIntoView) el.scrollIntoView({block: 'nearest'});
}

/* ------------------------------------------------ marking and coaching */
function byId(id){ for (var i = 0; i < ITEMS.length; i++) if (ITEMS[i].id === id) return ITEMS[i]; return EX[id] || null; }
function answered(it){ var a = S.ans[it.id]; return it.type === 'multi' ? !!(a && a.length) : a != null && String(a).trim() !== ''; }
function judge(it, triesSoFar){
  var a = S.ans[it.id];
  if (!answered(it)) return {v:'blank', what:[]};
  try {
    if (it.type === 'text') return C.feedback(it.part, a);
    if (it.type === 'mc') return C.mcFeedback(it.item, +a);
    return C.selectFeedback(it.item, a, (triesSoFar || 0) + 1);
  } catch(e){ return {v:'unread', what:['I can’t read that. Type a power with ^ and a fraction with /.']}; }
}
function res(it){ return S.res[it.id] || (S.res[it.id] = {tries:0, first:null, v:null, shown:false, hinted:false, steps:0, fb:null}); }
function record(it, f){
  var R = res(it);
  if (R.v === 'right') return R;
  R.tries++; R.v = f.v; R.fb = {what: f.what || [], rule: f.rule || '', step: f.step == null ? null : f.step};
  if (R.first === null) R.first = (f.v === 'right') && !R.hinted;
  if (it.extra){
    var M0 = S.more[it.base];
    if (f.v === 'right'){ M0.streak = R.first ? M0.streak + 1 : 0; if (M0.streak >= 2){ var ms = misses(); delete ms[it.pos]; store('misses', ms); } }
    else if (R.tries === 1) M0.streak = 0;
  } else if (R.tries === 1){                       /* only the first try decides a miss: fixing it later doesn't re-add a cleared one */
    var ms2 = misses(), fam = it.type === 'text' ? it.part.fam : it.item.fam;
    if (R.first === true) delete ms2[it.pos]; else if (R.first === false) ms2[it.pos] = fam || 1;
    store('misses', ms2);
  }
  return R;
}
function check(id){
  var it = byId(id); if (!it) return;
  if (S.mode === 'test' && !S.done && !it.extra) return;
  var R0 = S.res[it.id], f = judge(it, R0 ? R0.tries : 0);
  if (f.v === 'blank' || f.v === 'unread'){ flash(it, f); return; }
  if (!S.running && !S.done && !it.extra) start();
  record(it, f); save(); paintItem(it); paintScore();
  if (it.extra){ var hd = document.querySelector('.xq[data-q="' + it.id + '"] .xhead'); if (hd) hd.innerHTML = 'Try another like this' + streakHtml(S.more[it.base]); }
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
    var note = R.first ? '' : R.shown ? 'after seeing the steps' : R.hinted && R.tries === 1 ? 'with help' : 'on try ' + R.tries;
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
function solOf(it){ try { return it.type === 'text' ? C.solution(it.part) : C.mcSolution(it.item); } catch(e){ return null; } }
function picOf(it){
  try { var s = it.type === 'text' ? VZ.spec(it.part) : it.item.fam && it.item.fam !== 'select' ? VZ.spec({fam: it.item.fam, prm: it.item.prm}) : null; return s ? VZ.html(s) : ''; } catch(e){ return ''; }
}
function stepsHtml(it, R){
  var sol = solOf(it), n = sol ? sol.length : 0, shown = Math.min(R.steps || 0, n);
  var pic = (shown >= n || R.v === 'right') ? picOf(it) : '';    /* the picture states the answer: only with the full solution, or once it is right */
  var h = pic ? '<details class="why"' + (R.pic === false ? '' : ' open') + ' data-pic="' + it.id + '"><summary>See why it works</summary>' + pic + '</details>' : '';
  if (!sol) return h + '<div class="key"><span class="kl">Answer</span><span class="kv">' + keyHtml(it) + '</span></div>';
  var q = it.type === 'text' ? it.part.q : it.item.q, eq = it.type === 'text' && it.part.fam === 'solveN';
  var off = (R.v !== 'right' && R.fb && R.fb.step != null) ? R.fb.step : -1;
  h += q && it.type !== 'multi' ? '<div class="solhead"><span class="kl">Start</span> ' + E.M(q) + '</div>' : '';
  h += '<ol class="sol">' + sol.slice(0, shown).map(function(s, i){
    return '<li class="' + (i === off ? 'off' : '') + '"><div class="say">' + s.say + '</div>' +
      (s.ex ? '<div class="ex">' + (eq ? '' : '<span class="m">= </span>') + E.M(s.ex) + '</div>' : '') +
      (i === off ? '<div class="offnote">⟵ This is the step where your answer went off.</div>' : '') + '</li>';
  }).join('') + '</ol>';
  if (shown >= n) h += '<div class="key"><span class="kl">Answer</span><span class="kv">' + keyHtml(it) + '</span></div>';
  return h;
}
function hostOf(it){ return it.type === 'text' ? document.querySelector('.prt[data-id="' + it.id + '"]') : document.querySelector('.q[data-q="' + it.id + '"]'); }
function paintItem(it){
  var host = hostOf(it); if (!host) return;
  var R = S.res[it.id];
  var testHidden = S.mode === 'test' && !S.done && !it.extra;
  ['is-right','is-wrong','is-form'].forEach(function(c){ host.classList.remove(c); });
  var fb = $('fb' + it.id), mo = $('mo' + it.id), st = $('st' + it.id), wk = $('wk' + it.id);
  if (testHidden){ fb.hidden = true; mo.hidden = true; st.hidden = true; if (wk) wk.hidden = true; paintChoices(it, null); return; }
  var sol = solOf(it), n = sol ? sol.length : 1;
  R = R || {tries:0, v:null, steps:0};
  if (R.v) host.classList.add(R.v === 'right' ? 'is-right' : R.v === 'form' ? 'is-form' : 'is-wrong');
  if (R.v){ fb.innerHTML = cardHtml(it, R); fb.hidden = false; } else fb.hidden = true;
  var b = [], all = (R.steps || 0) >= n;
  if (R.v === 'right'){ if (!all) b.push('<button type="button" data-all="' + it.id + '">See the steps</button>'); }
  else {
    if (!all) b.push('<button type="button" data-hint="' + it.id + '">' + ((R.steps || 0) === 0 ? 'Hint' : 'Next step') + ' <span class="cnt">' + Math.min((R.steps || 0) + 1, n) + ' of ' + n + '</span></button>');
    if (!all && (R.tries > 0 || S.done)) b.push('<button type="button" data-all="' + it.id + '">Show me how</button>');
    if (false && it.type === 'text' && wk) b.push('<button type="button" data-work="' + it.id + '" aria-expanded="' + (!!(S.work && S.work[it.id] != null && S.workOpen && S.workOpen[it.id])) + '">Help me solve this</button>');
  }
  var missed = (R.v && R.v !== 'right') || R.shown || (R.v === 'right' && R.first === false);
  if (!it.extra && missed && !(S.more && S.more[it.id])) b.push('<button type="button" class="go" data-another="' + it.id + '">Try another like this</button>');
  if (it.extra && R.v === 'right') b.push('<button type="button" class="go" data-another="' + it.base + '">Another one</button>');
  if (!it.extra && S.more && S.more[it.id]) { /* the extra question is already showing below */ }
  mo.innerHTML = b.join(''); mo.hidden = !b.length;
  st.hidden = !(R.steps > 0); if (R.steps > 0) st.innerHTML = stepsHtml(it, R);
  if (wk){ var open = S.workOpen && S.workOpen[it.id]; wk.hidden = !open || R.v === 'right'; if (open && !wk.innerHTML) wk.innerHTML = workHtml(it); }
  paintChoices(it, R.v ? R : null);
  var input = $('a' + it.id); if (input) input.readOnly = R.v === 'right';
  var btn = host.querySelector('[data-check="' + it.id + '"]'); if (btn) btn.disabled = R.v === 'right';
  if (it.type !== 'text') Array.prototype.forEach.call(host.querySelectorAll('.ch input'), function(x){ x.disabled = R.v === 'right'; });
}
function paintChoices(it, R){
  if (it.type === 'text') return;
  it.item.opts.forEach(function(o, k){
    var ch = $('ch' + it.id + LET[k]); if (!ch) return; ch.classList.remove('picked-no','is-key');
    if (!R) return;
    var sol = solOf(it), all = sol && R.steps >= sol.length;
    var picked = it.type === 'mc' ? String(S.ans[it.id]) === String(k) : (S.ans[it.id] || []).map(Number).indexOf(k) >= 0;
    var isKey = it.type === 'mc' ? k === it.item.correct : it.item.correct.indexOf(k) >= 0;
    if (R.v === 'right' || all){ if (isKey) ch.classList.add('is-key'); }
    else if (picked && it.type === 'mc' && R.v === 'wrong') ch.classList.add('picked-no');
  });
}

/* ------------------------------------------------ "Help me solve this": the student's own work, checked line by line */
function workHtml(it){
  var p = it.part, eq = p.fam === 'solveN';
  return '<div class="wkhead"><b>Help me solve this</b><span>Type your work one step per line. Each line is checked against the question.</span></div>' +
    '<div class="solhead"><span class="kl">Start</span> ' + E.M(p.q) + '</div>' +
    '<textarea class="wta" id="wt' + it.id + '" data-kind="' + p.kind + '" rows="3" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="' + (eq ? 'like: n − 2 = 3' : 'like: ' + esc(sampleLine(p))) + '">' + esc((S.work && S.work[it.id]) || '') + '</textarea>' +
    '<div class="wbtn"><button type="button" class="go" data-wcheck="' + it.id + '">Check my work</button><button type="button" data-wuse="' + it.id + '">Use my last line as my answer</button></div>' +
    '<div class="wres" id="wr' + it.id + '" aria-live="polite"></div>' +
    (res(it).tries === 0 && !S.done && !it.extra ? '<p class="wnote">Checking your work before you check your answer counts as help, so this question won’t count as right on the first try.</p>' : '');
}
function sampleLine(p){ var sol = C.solution(p) || []; var s = sol.filter(function(x){ return x.ex; })[0]; return s ? C.typedOf(s.ex).replace(/\*/g, '·') : ''; }
function paintWork(it){
  var r = C.checkWork(it.part, (S.work && S.work[it.id]) || ''), box = $('wr' + it.id); if (!box) return;
  if (!r.lines.length){ box.innerHTML = '<p class="wmsg">Type a step first.</p>'; return; }
  var h = '<ol class="wlines">' + r.lines.map(function(l){
    var mark = l.ok === true ? '<span class="wok">✓</span>' : l.ok === false ? '<span class="wno">✗</span>' : '<span class="wq">?</span>';
    return '<li class="' + (l.ok === true ? 'ok' : l.ok === false ? 'no' : 'q') + '">' + mark + '<span class="wl">' + esc(l.raw) + '</span>' + (l.msg ? '<div class="wm">' + l.msg + '</div>' : '') + '</li>';
  }).join('') + '</ol>';
  if (r.finalMsg) h += '<p class="wfin' + (r.done ? ' done' : '') + '">' + r.finalMsg + '</p>';
  if (r.next) h += '<p class="wnext"><b>Next step:</b> ' + r.next.say + '</p>';
  box.innerHTML = h;
}

/* ------------------------------------------------ clicks */
document.addEventListener('click', function(e){
  var t = e.target.closest ? e.target : null; if (!t) return;
  var b = t.closest('[data-check]'); if (b){ check(b.dataset.check); return; }
  var h = t.closest('[data-hint]');
  if (h){ var it = byId(h.dataset.hint), R = res(it);
    if (R.tries === 0 && (!S.done || it.extra)) R.hinted = true;
    R.steps = (R.steps || 0) + 1;
    var sol = solOf(it); if (sol && R.steps >= sol.length && R.v !== 'right'){ R.shown = true; if (R.first === null) R.first = false; }
    if (!S.running && !S.done && !it.extra) start();
    save(); paintItem(it); paintScore(); return; }
  var a = t.closest('[data-all]');
  if (a){ var it2 = byId(a.dataset.all), R2 = res(it2), sol2 = solOf(it2);
    R2.steps = sol2 ? sol2.length : 1;
    if (R2.v !== 'right'){ R2.shown = true; if (R2.first === null) R2.first = false; }
    save(); paintItem(it2); paintScore(); return; }
  var w = t.closest('[data-work]');
  if (w){ var it3 = byId(w.dataset.work); S.workOpen = S.workOpen || {}; S.workOpen[it3.id] = !S.workOpen[it3.id]; S.work = S.work || {};
    var wk = $('wk' + it3.id); if (S.workOpen[it3.id]){ wk.innerHTML = workHtml(it3); if (S.work[it3.id]) paintWork(it3); }
    save(); paintItem(it3); if (S.workOpen[it3.id]){ var ta = $('wt' + it3.id); if (ta) ta.focus(); } return; }
  var wc = t.closest('[data-wcheck]');
  if (wc){ var it4 = byId(wc.dataset.wcheck), R4 = res(it4);
    if (R4.tries === 0 && (!S.done || it4.extra)){ R4.hinted = true; if (!S.running && !S.done && !it4.extra) start(); }
    S.work[it4.id] = $('wt' + it4.id).value; save(); paintWork(it4); paintScore(); return; }
  var wu = t.closest('[data-wuse]');
  if (wu){ var it5 = byId(wu.dataset.wuse), lines = ($('wt' + it5.id).value || '').split('\n').map(function(x){ return x.trim(); }).filter(Boolean);
    if (!lines.length) return; var lastL = lines[lines.length - 1].split('=').map(function(x){ return x.trim(); }).filter(Boolean);
    var v = lastL[lastL.length - 1];
    if (it5.part.fam === 'solveN' && lastL.length === 2 && /^n$/i.test(lastL[1])) v = lastL[0];
    var inp = $('a' + it5.id); inp.value = v; inp.dispatchEvent(new Event('input', {bubbles: true})); inp.focus(); return; }
  var an = t.closest('[data-another]'); if (an){ another(an.dataset.another); return; }
  var nw = t.closest('[data-new]'); if (nw){ var sc = nw.dataset.scope || scope;
    if (started() && !S.done) ask('Leave this set? It stays saved on this device.', 'New set', function(){ openSet(randomSeed(), sc); }); else openSet(randomSeed(), sc); return; }
});
document.addEventListener('toggle', function(e){ var d = e.target; if (d && d.dataset && d.dataset.pic){ var R = res(byId(d.dataset.pic)); R.pic = d.open; save(); } }, true);

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
  var t = e.target;
  if (t.matches && t.matches('#paper input[type=text], #paper textarea.wta') && !t.readOnly){ keys.target = t; (t.tagName === 'TEXTAREA' ? t.parentNode.insertBefore(keys, t.nextSibling) : t.parentNode.appendChild(keys)); keys.hidden = false; }
  else if (!(t.closest && t.closest('.keys'))) keys.hidden = true;
});
document.addEventListener('input', function(e){
  var t = e.target;
  if (t.classList && t.classList.contains('wta')){ S.work = S.work || {}; S.work[t.id.slice(2)] = t.value; save(); return; }
  if (!t.id || t.id.charAt(0) !== 'a' || !t.closest('#paper')) return;
  var it = byId(t.id.slice(1)); if (!it) return;
  if (!S.running && !S.done && !it.extra) start();
  S.ans[it.id] = t.value; setPreview(t);
  save(); paintProgress();
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Enter' && e.target.matches && e.target.matches('#paper input[type=text]')){ e.preventDefault(); var it = byId(e.target.id.slice(1)); if (it && (S.mode === 'practice' || S.done || it.extra)) check(it.id); }
});
document.addEventListener('change', function(e){
  var t = e.target; if (!t.name || t.name.charAt(0) !== 'q' || !t.closest('#paper')) return;
  var id = t.name.slice(1), it = byId(id); if (!it) return;
  if (!S.running && !S.done && !it.extra) start();
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
  var first = 0, done = 0, bySec = DS.map(function(){ return {got:0, of:0}; });
  ITEMS.forEach(function(it){ var R = S.res[it.id]; bySec[it.sec].of++; if (R && R.first === true){ first++; bySec[it.sec].got++; } if (R && R.v === 'right') done++; });
  return {first:first, done:done, bySec:bySec};
}
function paintProgress(){ var n = ITEMS.filter(answered).length; $('prog').style.width = (ITEMS.length ? 100*n/ITEMS.length : 0) + '%'; return n; }
function paintScore(){
  var t = tally(), sc = $('score');
  if (S.mode === 'test' && !S.done) sc.innerHTML = '<b>' + ITEMS.filter(answered).length + ' of ' + ITEMS.length + '</b> answered · marked when you finish';
  else sc.innerHTML = 'First try <b>' + t.first + ' / ' + ITEMS.length + '</b> · solved <b>' + t.done + '</b>';
  paintResult(t); paintScopes();
}
function paintBar(){
  $('time').textContent = fmt(elapsed());
  $('bStart').hidden = S.done || S.running; $('bStart').textContent = elapsed() > 0 ? 'Resume' : 'Start';
  $('bPause').hidden = S.done || !S.running;
  $('bFinish').hidden = S.done || !ITEMS.length;
  $('bFinish').textContent = S.mode === 'test' ? 'Finish & mark' : 'Finish';
  document.body.classList.toggle('hidechk', S.mode === 'test' && !S.done);
  Array.prototype.forEach.call(document.querySelectorAll('.mode button'), function(b){ b.setAttribute('aria-pressed', String(b.dataset.mode === S.mode)); });
}
function paintResult(t){
  var box = $('result');
  if (!S.done){ box.hidden = true; return; }
  var rows = DS.map(function(s, k){ return '<tr><td>' + s.title + '</td><td class="r">' + t.bySec[k].got + ' / ' + t.bySec[k].of + '</td></tr>'; }).join('');
  var weakParts = {};
  ITEMS.forEach(function(it){ var R = S.res[it.id]; if (!R || R.first !== true) weakParts[+it.pos.split('.')[0]] = (weakParts[+it.pos.split('.')[0]] || 0) + 1; });
  var nm = Object.keys(misses()).length;
  var btns = Object.keys(weakParts).sort().map(function(k){ return '<button type="button" data-new="1" data-scope="p' + (+k + 1) + '">Practice Part ' + (+k + 1) + '</button>'; }).join('') +
    (nm ? '<button type="button" data-new="1" data-scope="miss">My misses (' + nm + ')</button>' : '') + '<button type="button" class="go" data-new="1" data-scope="all">New whole test</button>';
  box.innerHTML = '<h2>Set ' + seed + ' · ' + esc(SCOPES[scope]) + ' · ' + (S.mode === 'test' ? 'test style' : 'checked as you went') + '</h2>' +
    '<div class="big"><div><b>' + t.first + '<small> / ' + ITEMS.length + '</small></b><span>right on the first try</span></div><div><b>' + fmt(S.acc) + '</b><span>time on the clock</span></div></div>' +
    '<div class="tw"><table><thead><tr><th>Part</th><th class="r">First try</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
    '<p class="note">Fix the ones that aren’t right yet — <b>Show me how</b> has the steps and a picture of why, and <b>Try another like this</b> gives you a fresh one. Or practice just what you need:</p>' +
    '<div class="btns">' + btns + '</div>';
  box.hidden = false;
}
function finish(){
  if (S.running) S.acc = elapsed(); S.running = false; S.startedAt = null; S.done = true;
  if (S.mode === 'test'){ ITEMS.forEach(function(it){ var R = res(it), f = judge(it, R.tries);
      if (f.v === 'blank' || f.v === 'unread'){ R.first = false; R.v = 'wrong'; R.tries = 1; R.fb = {what: [f.v === 'blank' ? 'Left blank.' : (f.what[0] || 'Could not read the answer.')], rule: '', step: null};
        var ms = misses(); ms[it.pos] = (it.part || it.item).fam || 1; store('misses', ms); }
      else record(it, f); }); }
  else ITEMS.forEach(function(it){ var R = res(it); if (R.first === null) R.first = false; });   /* skipped in practice: not a miss, just not done */
  save(); paintAll(); window.scrollTo(0, 0);
}

/* ------------------------------------------------ sets */
function ask(text, yes, fn){
  var c = $('confirm'); c.hidden = false;
  c.innerHTML = '<span>' + text + '</span><button type="button" class="go" id="cy">' + yes + '</button><button type="button" id="cn">Cancel</button>';
  $('cy').onclick = function(){ c.hidden = true; fn(); }; $('cn').onclick = function(){ c.hidden = true; };
}
function started(){ return elapsed() > 0 || ITEMS.some(answered) || Object.keys(S.res).length > 0; }
function openSet(n, sc){
  if (S) pause();
  seed = n; scope = SCOPES[sc] ? sc : 'all';
  var saved = load(key());
  if (scope === 'miss' && !(saved && saved.res)){ var pos = Object.keys(misses()); if (!pos.length){ scope = 'all'; saved = load(key()); } }
  S = saved && saved.res ? saved : fresh((S && S.mode) || 'practice');
  if (scope === 'miss' && !S.pos) S.pos = Object.keys(misses());
  S.work = S.work || {}; S.more = S.more || {}; S.running = false; S.startedAt = null;
  try { history.replaceState(null, '', '#set-' + seed + (scope === 'all' ? '' : '-' + scope)); } catch(e){}
  render(); restore(); save(); paintAll(); window.scrollTo(0, 0);
}
function restoreOne(it){
  var a = S.ans[it.id]; if (a == null) return;
  if (it.type === 'text'){ var el = $('a' + it.id); if (el){ el.value = a; setPreview(el); } }
  else (it.type === 'mc' ? [a] : a).forEach(function(v){ var x = document.querySelector('input[name="q' + it.id + '"][value="' + v + '"]'); if (x) x.checked = true; });
}
function restore(){ ITEMS.forEach(restoreOne); }
function paintAll(){
  paintScopes(); paintBar(); paintProgress(); ITEMS.forEach(paintItem); Object.keys(EX).forEach(function(k){ paintItem(EX[k]); });
  ITEMS.concat(Object.keys(EX).map(function(k){ return EX[k]; })).forEach(function(it){ if (S.workOpen && S.workOpen[it.id] && S.work[it.id]){ var wk = $('wk' + it.id); if (wk && !wk.innerHTML) wk.innerHTML = workHtml(it); paintWork(it); } });
  paintScore();
}
$('bStart').addEventListener('click', start);
$('bPause').addEventListener('click', pause);
$('bFinish').addEventListener('click', function(){
  var left = ITEMS.length - ITEMS.filter(answered).length;
  ask((left ? left + ' of ' + ITEMS.length + ' still blank. ' : '') + (S.mode === 'test' ? 'Stop the clock and mark everything?' : 'Stop the clock and see your score?'), 'Finish', finish);
});
Array.prototype.forEach.call(document.querySelectorAll('.mode button'), function(b){
  b.addEventListener('click', function(){
    var m = b.dataset.mode; if (m === S.mode) return;
    var go = function(){ var pos = S.pos; drop(key()); S = fresh(m); if (pos) S.pos = pos; render(); save(); paintAll(); };
    if (started()) ask('Switching starts this set over. Your answers will be cleared.', 'Switch', go); else go();
  });
});
$('scope').addEventListener('change', function(){ var v = this.value; if (v === scope) return;
  if (started() && !S.done) ask('Switch to “' + SCOPES[v] + '”? This set stays saved on this device.', 'Switch', function(){ openSet(seed, v); }, function(){});
  else openSet(seed, v);
  $('scope').value = scope; });
$('setgo').addEventListener('click', function(){ var v = Math.floor(+$('setin').value); if (v >= 1 && v <= 99999) openSet(v, scope); else { $('setin').value = seed; } });
$('setin').addEventListener('keydown', function(e){ if (e.key === 'Enter'){ e.preventDefault(); $('setgo').click(); } });
$('bAgain').addEventListener('click', function(){ ask('Clear your answers to this set and start it again?', 'Start over', function(){ var m = S.mode, pos = S.pos; drop(key()); S = fresh(m); if (pos) S.pos = pos; render(); save(); paintAll(); window.scrollTo(0,0); }); });
window.addEventListener('hashchange', function(){ var h = fromHash(); if (h && (h.seed !== seed || h.scope !== scope)) openSet(h.seed, h.scope); });
setInterval(function(){ if (S && S.running) $('time').textContent = fmt(elapsed()); }, 500);
window.addEventListener('pagehide', function(){ if (S && S.running){ S.acc = elapsed(); S.startedAt = now(); save(); } });

openSet(seed, scope);
})();
