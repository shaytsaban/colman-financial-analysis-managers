/* Meeting 4 on (2026-11-24): autofit. Loaded only when LMETA autofit is on, so taught decks rebuild byte-identical. */
/* ---------- autofit (Shay, 2026-11-24: "large parts of the slides stay empty"): the body of a content slide is scaled up, at most
   1.4 times, until it reaches the footer. It is measured with every reveal shown and every answer explanation open, so nothing
   overflows later. Slides are laid out even while hidden, so all of them are fitted at load, and again once the fonts are in. ---------- */
(function(){
 function fitOne(s){const w=s.querySelector(':scope > .afit');if(!w)return;
  const cs=getComputedStyle(s),cw=s.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
  const limit=(s.querySelector('.ft')?720-36:716)-8,top=()=>s.getBoundingClientRect().top;
  const k0=(s.getBoundingClientRect().height/720)||1;
  const bottom=()=>(w.getBoundingClientRect().bottom-top())/k0;
  const set=z=>{w.style.zoom=z;w.style.width=(cw/z)+'px';};
  const hid=[...s.querySelectorAll('.st:not(.show)')];hid.forEach(e=>e.classList.add('show'));s.classList.add('afm');set(1);
  if(bottom()<=limit){let lo=1,hi=1.4;for(let i=0;i<10;i++){const m=(lo+hi)/2;set(m);if(bottom()<=limit)lo=m;else hi=m;}set(lo);}
  s.classList.remove('afm');hid.forEach(e=>e.classList.remove('show'));}
 const all=()=>document.querySelectorAll('.slide').forEach(fitOne);
 all();addEventListener('load',()=>{all();setTimeout(all,600);});if(document.fonts&&document.fonts.ready)document.fonts.ready.then(all);
 window.__autofit=all;
})();
