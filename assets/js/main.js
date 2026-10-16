const qs=(s,c=document)=>c.querySelector(s), qsa=(s,c=document)=>[...c.querySelectorAll(s)];
const header=qs('.site-header');
const menuBtn=qs('.menu-button'), mobileMenu=qs('.mobile-menu');
const PHONE='2348033949943';
window.addEventListener('scroll',()=>header?.classList.toggle('scrolled',window.scrollY>24),{passive:true});
if(menuBtn&&mobileMenu){menuBtn.addEventListener('click',()=>{const open=mobileMenu.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));mobileMenu.setAttribute('aria-hidden',String(!open));});}
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -6% 0px'});
qsa('.reveal').forEach(el=>observer.observe(el));
const glow=qs('.cursor-glow');
if(glow && matchMedia('(pointer:fine)').matches){window.addEventListener('pointermove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px';},{passive:true});}
qsa('.tilt').forEach(card=>{if(!matchMedia('(pointer:fine)').matches)return;const base=card.style.transform;card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;card.style.transform=`${base} rotateX(${(-y*4).toFixed(2)}deg) rotateY(${(x*5).toFixed(2)}deg) translateY(-3px)`});card.addEventListener('mouseleave',()=>card.style.transform=base);});
const filters=qsa('.filter'), cards=qsa('[data-project-grid] .project-card');
filters.forEach(btn=>btn.addEventListener('click',()=>{filters.forEach(b=>b.classList.remove('active'));btn.classList.add('active');const f=btn.dataset.filter;cards.forEach(c=>c.classList.toggle('is-hidden',f!=='all'&&c.dataset.category!==f));}));
qsa('[data-whatsapp-form]').forEach(form=>form.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(form);const msg=[`Hi RIID, I'd like to discuss a project.`,``,`Name: ${d.get('name')}`,`Business: ${d.get('business')}`,`Project: ${d.get('service')}`,`Budget: ${d.get('budget')}`,`Timeline: ${d.get('timeline')}`,``,`Brief: ${d.get('brief')}`].join('\n');window.open(`https://wa.me/${PHONE}?text=${encodeURIComponent(msg)}`,'_blank','noopener');}));
