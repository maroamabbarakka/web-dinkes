'use strict';
// Manual feature switching: intentionally no auto-rotation (accessibility and performance).
(function(){
  const slides=Array.from(document.querySelectorAll('.v4-feature-slide'));
  if(!slides.length)return;
  const dots=Array.from(document.querySelectorAll('[data-slide-to]'));
  const rail=document.querySelector('.v4-feature-rail');
  let index=0;
  function show(next,focus=false){
    index=(next+slides.length)%slides.length;
    slides.forEach((slide,i)=>{
      const selected=i===index;
      slide.hidden=!selected;slide.classList.toggle('is-active',selected);
      slide.setAttribute('aria-hidden',String(!selected));
      slide.querySelectorAll('a,button').forEach(a=>{a.tabIndex=selected?0:-1});
    });
    dots.forEach((dot,i)=>{
      const selected=i===index;
      dot.classList.toggle('active',selected);
      if(selected){dot.setAttribute('aria-current','true');if(focus)dot.focus()}
      else dot.removeAttribute('aria-current');
    });
  }
  dots.forEach(d=>d.addEventListener('click',()=>show(Number(d.dataset.slideTo))));
  document.querySelectorAll('[data-slide-step]').forEach(btn=>btn.addEventListener('click',()=>show(index+Number(btn.dataset.slideStep))));
  rail?.addEventListener('keydown',e=>{
    if(e.target?.closest('.v4-slide-dots') && (e.key==='ArrowLeft'||e.key==='ArrowRight')){
      e.preventDefault();show(index+(e.key==='ArrowRight'?1:-1),true);
    }
  });
  show(0);
})();
