from pathlib import Path
import html, json

ROOT = Path('/mnt/data/riid_final')
PHONE_DISPLAY = '+234 803 394 9943'
PHONE_WA = '2348033949943'

projects = [
    {
        'slug':'kingsbridge-legal','name':'Kingsbridge Legal Partners','industry':'Legal Services','category':'professional','accent':'#d8b06b',
        'tagline':'Authority, discretion and clarity — translated into a premium digital presence.',
        'summary':'A prestige-led concept for a Nigerian commercial law firm serving founders, institutions and high-value businesses.',
        'features':['Editorial legal positioning','Practice-area storytelling','Consultation-first conversion path','Executive mobile experience'],
        'visual':'Deep navy, warm ivory, muted gold, editorial serif typography and formal Nigerian corporate imagery.',
        'image':'/assets/mockups/kingsbridge-legal.jpg'
    },
    {
        'slug':'harbourline-logistics','name':'Harbourline Logistics','industry':'Shipping & Logistics','category':'logistics','accent':'#ff6b1a',
        'tagline':'A bolder digital system for a logistics company moving goods across Nigeria and beyond.',
        'summary':'An industrial, conversion-focused logistics concept built around credibility, quote requests and shipment visibility.',
        'features':['Freight solution hierarchy','Quote-driven user journey','Tracking-focused interface','Apapa-to-nationwide visual language'],
        'visual':'Midnight blue, safety orange, technical grids, port photography and motion-led route cues.',
        'image':'/assets/mockups/harbourline-logistics.jpg'
    },
    {
        'slug':'suncrest-energy','name':'Suncrest Energy','industry':'Solar & Energy','category':'energy','accent':'#2c8cff',
        'tagline':'Clean power presented with the confidence of a serious engineering brand.',
        'summary':'A modern solar concept for Nigerian homes, estates and businesses, designed to move visitors toward assessments and WhatsApp enquiries.',
        'features':['Residential & commercial pathways','System sizing narrative','WhatsApp quote handoff','Nigerian installation imagery'],
        'visual':'Royal blue, white, sky blue and restrained yellow with crisp technical typography and solar imagery.',
        'image':'/assets/mockups/suncrest-energy.jpg'
    },
    {
        'slug':'primeflow-plumbing','name':'PrimeFlow Plumbing','industry':'Home Services','category':'services','accent':'#ff5b2e',
        'tagline':'Fast answers, clear service choices and a booking journey built for urgent customers.',
        'summary':'A practical premium concept for a Lagos plumbing and emergency maintenance business where speed and trust matter most.',
        'features':['Emergency-first CTA system','Service category chooser','Booking-oriented mobile layout','Location-led credibility'],
        'visual':'Deep teal, warm white and high-visibility orange with friendly technician photography and direct UX.',
        'image':'/assets/mockups/primeflow-plumbing.jpg'
    },
    {
        'slug':'northstone-properties','name':'Northstone Properties','industry':'Luxury Real Estate','category':'real-estate','accent':'#c8a471',
        'tagline':'Architecture, aspiration and enquiry — presented like a premium property brand.',
        'summary':'An editorial real-estate concept for luxury homes in Lekki, Ikoyi, Victoria Island, Abuja and other premium Nigerian markets.',
        'features':['Property discovery UX','Inspection-led conversion','Location-focused storytelling','Luxury editorial presentation'],
        'visual':'Off-white, charcoal and champagne with cinematic architecture, restrained type and generous whitespace.',
        'image':'/assets/mockups/northstone-properties.jpg'
    },
    {
        'slug':'ivory-dental','name':'Ivory Dental Studio','industry':'Healthcare','category':'healthcare','accent':'#6cc8d8',
        'tagline':'A calm, reassuring digital experience designed around patient confidence.',
        'summary':'A modern private dental concept built to simplify treatment discovery and appointment enquiries for Nigerian patients.',
        'features':['Treatment-led information design','Appointment pathway','Dentist profile system','Mobile-first patient experience'],
        'visual':'Soft white, pale blue and sage with rounded details, bright clinical imagery and calm pacing.',
        'image':'/assets/mockups/ivory-dental.jpg'
    },
    {
        'slug':'stonebridge-developments','name':'Stonebridge Developments','industry':'Construction & Architecture','category':'construction','accent':'#df7b45',
        'tagline':'A digital portfolio that makes serious construction work feel as considered as the buildings themselves.',
        'summary':'An architecture-led concept for Nigerian developers and construction firms selling capability through projects, process and detail.',
        'features':['Project-led portfolio system','Construction capability storytelling','Timeline visual language','High-intent enquiry journey'],
        'visual':'Architectural black, warm grey, cream and terracotta with asymmetrical grids and project-led photography.',
        'image':'/assets/mockups/stonebridge-developments.jpg'
    },
    {
        'slug':'copper-table','name':'Copper Table','industry':'Restaurant & Hospitality','category':'hospitality','accent':'#c14e2b',
        'tagline':'Warm hospitality, modern Nigerian flavour and a visual identity people remember.',
        'summary':'A premium dining concept shaped around food discovery, reservations, private dining and catering enquiries.',
        'features':['Food-first editorial design','Reservation conversion','Menu storytelling','Private event positioning'],
        'visual':'Burgundy, burnt orange, cream and dark brown with rich food imagery and expressive editorial typography.',
        'image':'/assets/mockups/copper-table.jpg'
    },
    {
        'slug':'crown-and-loom','name':'Crown & Loom','industry':'Fashion & E-commerce','category':'commerce','accent':'#aa5a3c',
        'tagline':'A Nigerian fashion concept with the confidence of an international luxury label.',
        'summary':'A high-fashion e-commerce direction built around collections, product discovery and editorial storytelling.',
        'features':['Collection-led shopping','Editorial campaign moments','Product-focused conversion','Premium mobile commerce'],
        'visual':'Ivory, black and burnt sienna with full-bleed fashion photography and high-fashion typography.',
        'image':'/assets/mockups/crown-and-loom.jpg'
    },
    {
        'slug':'apex-motorworks','name':'Apex Motorworks','industry':'Automotive Service','category':'automotive','accent':'#ff641e',
        'tagline':'Performance, precision and service confidence for modern Nigerian drivers.',
        'summary':'A cinematic automotive concept for a premium service centre handling diagnostics, maintenance and performance work.',
        'features':['Vehicle service booking','Package comparison','Workshop credibility','Performance-led visual system'],
        'visual':'Matte black, off-white and electric orange with bold geometry, workshop imagery and technical motion.',
        'image':'/assets/mockups/apex-motorworks.jpg'
    },
    {
        'slug':'westbridge-academy','name':'Westbridge Academy','industry':'Private Education','category':'education','accent':'#f0b33a',
        'tagline':'A clearer, warmer digital home for a modern Nigerian school community.',
        'summary':'A trust-led education concept for admissions, academics, school life and parent enquiries.',
        'features':['Admissions pathway','Academic programme structure','School-life storytelling','Parent-friendly mobile navigation'],
        'visual':'Navy, warm white and mustard with optimistic campus imagery and structured information design.',
        'image':'/assets/mockups/westbridge-academy.jpg'
    },
    {
        'slug':'stone-and-linen','name':'Stone & Linen Interiors','industry':'Interior Design','category':'interiors','accent':'#9b9278',
        'tagline':'A quiet, luxurious portfolio for spaces designed to be lived in.',
        'summary':'A minimalist interior design concept built around project imagery, consultation enquiries and tasteful editorial pacing.',
        'features':['Project gallery storytelling','Before/after direction','Consultation CTA system','Editorial image-led layouts'],
        'visual':'Sand, stone, black and muted olive with oversized interior photography and restrained typography.',
        'image':'/assets/mockups/stone-and-linen.jpg'
    },
]

project_by_slug = {p['slug']:p for p in projects}

NAV = [('/','Home'),('/work/','Work'),('/services/','Services'),('/about/','About'),('/contact/','Contact')]

def head(title, desc, path='/', accent='#2b7fff'):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#07090d">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="alternate icon" href="/favicon.svg">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
<style>:root{{--page-accent:{accent}}}</style>
</head>
<body data-path="{path}">
<div class="page-noise" aria-hidden="true"></div>
<div class="cursor-glow" aria-hidden="true"></div>
'''

def nav(active=''):
    links=''.join([f'<a href="{href}" class="{("active" if label.lower()==active.lower() else "")}">{label}</a>' for href,label in NAV])
    return f'''
<header class="site-header">
  <a class="brand" href="/" aria-label="RIID home"><span class="brand-mark">R</span><span class="brand-name">RIID</span></a>
  <nav class="desktop-nav">{links}</nav>
  <a class="header-cta" href="/start/">Start a project <span>↗</span></a>
  <button class="menu-button" aria-label="Open navigation" aria-expanded="false"><span></span><span></span></button>
</header>
<div class="mobile-menu" aria-hidden="true">
  <div>{links}</div>
  <a class="button primary full" href="/start/">Start a project ↗</a>
</div>
'''

def footer():
    return f'''
<footer class="site-footer">
  <div class="footer-top">
    <div><div class="footer-brand">RIID</div><p>Digital experiences for ambitious businesses.</p></div>
    <div class="footer-nav"><a href="/work/">Work</a><a href="/services/">Services</a><a href="/about/">About</a><a href="/contact/">Contact</a></div>
    <a class="whatsapp-link" href="https://wa.me/{PHONE_WA}?text=Hi%20RIID%2C%20I%27d%20like%20to%20discuss%20a%20website%20project." target="_blank" rel="noopener">WhatsApp <span>{PHONE_DISPLAY}</span> ↗</a>
  </div>
  <div class="footer-bottom"><span>© 2026 RIID. Lagos, Nigeria.</span><span>Built here. Designed to compete anywhere.</span></div>
</footer>
<script src="/assets/js/main.js" defer></script>
</body></html>'''


def project_card(p, size='normal'):
    return f'''
<a class="project-card {size}" href="/work/{p['slug']}/" data-category="{p['category']}">
  <div class="project-image-wrap">
    <img loading="lazy" src="{p['image']}" alt="{html.escape(p['name'])} website concept mockup">
    <div class="project-shade"></div>
    <span class="concept-pill">Concept project</span>
    <span class="view-project">View project <b>↗</b></span>
  </div>
  <div class="project-meta">
    <div><h3>{p['name']}</h3><p>{p['industry']}</p></div>
    <span>0{projects.index(p)+1}</span>
  </div>
</a>'''


def home_page():
    feature = [project_by_slug['suncrest-energy'], project_by_slug['northstone-properties'], project_by_slug['harbourline-logistics']]
    cards=''.join(project_card(p,'featured') for p in feature)
    return head('RIID — Premium websites for ambitious businesses','RIID is a Nigerian digital studio creating premium, conversion-focused websites and digital experiences for growing businesses.','/','#2b7fff') + nav('Home') + f'''
<main>
<section class="home-hero">
  <div class="hero-copy reveal">
    <span class="eyebrow"><i></i> Lagos, Nigeria · Digital Studio</span>
    <h1>Websites that make businesses <em>look serious.</em></h1>
    <p>RIID designs premium digital experiences that help growing businesses earn trust, generate enquiries and move customers to action.</p>
    <div class="hero-actions"><a class="button primary" href="/start/">Start a project ↗</a><a class="button ghost" href="/work/">Explore our work</a></div>
    <div class="hero-proof"><span>Strategy</span><span>Design</span><span>Development</span><span>Conversion</span></div>
  </div>
  <div class="hero-stage reveal delay-1" aria-label="Selected RIID work">
    <a href="/work/suncrest-energy/" class="floating-mockup mockup-main tilt"><img src="/assets/mockups/suncrest-energy.jpg" alt="Suncrest Energy concept"></a>
    <a href="/work/northstone-properties/" class="floating-mockup mockup-one tilt"><img src="/assets/mockups/northstone-properties.jpg" alt="Northstone Properties concept"></a>
    <a href="/work/apex-motorworks/" class="floating-mockup mockup-two tilt"><img src="/assets/mockups/apex-motorworks.jpg" alt="Apex Motorworks concept"></a>
    <div class="stage-label"><span>Selected work</span><b>12 industries</b></div>
  </div>
  <a href="#selected" class="scroll-cue">Scroll <span>↓</span></a>
</section>

<section class="statement-band reveal">
  <span>NOT ANOTHER TEMPLATE.</span>
  <p>Every project gets its own visual language, structure and conversion strategy.</p>
</section>

<section id="selected" class="section selected-work">
  <div class="section-heading reveal"><div><span class="eyebrow"><i></i> Selected work</span><h2>Different industries.<br><em>Different identities.</em></h2></div><a class="text-link" href="/work/">See all 12 projects ↗</a></div>
  <div class="featured-grid">{cards}</div>
</section>

<section class="section capabilities">
  <div class="capabilities-intro reveal"><span class="eyebrow"><i></i> What RIID builds</span><h2>Digital work designed around the business — not around a template.</h2></div>
  <div class="capability-list">
    <a href="/services/#business-websites" class="capability-row reveal"><span>01</span><h3>Business websites</h3><p>Premium multi-page websites that build trust and turn attention into enquiries.</p><b>↗</b></a>
    <a href="/services/#commerce" class="capability-row reveal"><span>02</span><h3>E-commerce</h3><p>Product experiences designed to make discovery, confidence and buying feel effortless.</p><b>↗</b></a>
    <a href="/services/#conversion" class="capability-row reveal"><span>03</span><h3>Conversion systems</h3><p>Landing pages, lead funnels, WhatsApp journeys and business-focused digital flows.</p><b>↗</b></a>
  </div>
</section>

<section class="nigeria-section reveal">
  <div><span class="eyebrow light"><i></i> Nigerian-rooted</span><h2>Built here.<br><em>Designed to compete anywhere.</em></h2></div>
  <p>We build for the way Nigerian customers actually browse, compare, ask questions and buy — while keeping the visual standard global.</p>
  <div class="ng-cities"><span>Lagos</span><span>Abuja</span><span>Port Harcourt</span><span>Ibadan</span><span>Nationwide</span></div>
</section>

<section class="cta-section reveal"><span>Have something worth building?</span><h2>Let’s make your business look as good as the work you do.</h2><a class="button light" href="/start/">Start a project ↗</a></section>
</main>
''' + footer()


def work_page():
    sizes=['wide','tall','normal','normal','wide','tall','normal','wide','normal','normal','tall','wide']
    cards=''.join(project_card(p,s) for p,s in zip(projects,sizes))
    return head('Work — RIID','Explore RIID concept projects across Nigerian industries including solar, real estate, logistics, legal, healthcare, fashion and more.','/work/','#2b7fff') + nav('Work') + f'''
<main>
<section class="page-hero work-hero reveal"><span class="eyebrow"><i></i> RIID Portfolio</span><h1>Selected work.<br><em>Real businesses. Different industries.</em></h1><p>Concept directions created to show how RIID can give each business its own identity — not the same website with another colour.</p></section>
<section class="work-filter-wrap"><div class="work-filters" role="group" aria-label="Filter projects">
<button class="filter active" data-filter="all">All</button><button class="filter" data-filter="professional">Legal</button><button class="filter" data-filter="logistics">Logistics</button><button class="filter" data-filter="energy">Energy</button><button class="filter" data-filter="real-estate">Real estate</button><button class="filter" data-filter="commerce">Commerce</button><button class="filter" data-filter="healthcare">Healthcare</button><button class="filter" data-filter="services">Services</button><button class="filter" data-filter="construction">Construction</button><button class="filter" data-filter="hospitality">Hospitality</button><button class="filter" data-filter="automotive">Automotive</button><button class="filter" data-filter="education">Education</button><button class="filter" data-filter="interiors">Interiors</button>
</div></section>
<section class="work-grid" data-project-grid>{cards}</section>
<section class="cta-section compact reveal"><span>Seen a direction you like?</span><h2>We’ll build yours around your business — not around theirs.</h2><a class="button light" href="/start/">Start a project ↗</a></section>
</main>
''' + footer()


def services_page():
    return head('Services — RIID','Premium web design, e-commerce, website redesign and conversion-focused digital solutions from RIID.','/services/','#2b7fff') + nav('Services') + f'''
<main>
<section class="page-hero services-hero reveal"><span class="eyebrow"><i></i> Services</span><h1>Websites with a job to do.</h1><p>RIID combines strategy, design and development to create digital experiences that look premium and move people toward action.</p></section>
<section class="service-stack">
  <article id="business-websites" class="service-panel reveal"><div class="service-num">01</div><div><span>Business websites</span><h2>Make the business feel established before the first conversation.</h2></div><div><p>Multi-page websites for service companies, professional firms and growing brands that need stronger credibility and more enquiries.</p><ul><li>Strategy & page architecture</li><li>Custom UI/UX design</li><li>Responsive development</li><li>WhatsApp & lead forms</li><li>Basic search setup</li></ul></div></article>
  <article id="commerce" class="service-panel reveal"><div class="service-num">02</div><div><span>E-commerce</span><h2>Turn products into a buying experience people trust.</h2></div><div><p>Product-led storefronts for fashion, gadgets, lifestyle and retail brands with clear discovery, product presentation and checkout journeys.</p><ul><li>Collection architecture</li><li>Product page design</li><li>Cart & checkout UX</li><li>Mobile commerce</li><li>Payment integration readiness</li></ul></div></article>
  <article id="conversion" class="service-panel reveal"><div class="service-num">03</div><div><span>Conversion systems</span><h2>Make every click lead somewhere useful.</h2></div><div><p>Landing pages and lead funnels designed around enquiries, bookings, quotations and WhatsApp conversations.</p><ul><li>Campaign landing pages</li><li>Quote & booking flows</li><li>WhatsApp handoff</li><li>Form optimisation</li><li>Analytics-ready structure</li></ul></div></article>
</section>
<section class="process-section section">
  <div class="section-heading reveal"><div><span class="eyebrow"><i></i> Process</span><h2>Clear from first call to launch.</h2></div></div>
  <div class="process-grid"><div class="process-step reveal"><b>01</b><h3>Understand</h3><p>Business, audience, goals and what customers need to do.</p></div><div class="process-step reveal"><b>02</b><h3>Direction</h3><p>Structure, messaging, art direction and conversion strategy.</p></div><div class="process-step reveal"><b>03</b><h3>Design</h3><p>Custom desktop and mobile experience — no recycled template.</p></div><div class="process-step reveal"><b>04</b><h3>Build</h3><p>Responsive development, interaction and lead-flow implementation.</p></div><div class="process-step reveal"><b>05</b><h3>Launch</h3><p>Final checks, handoff and support after the website goes live.</p></div></div>
</section>
<section class="cta-section reveal"><span>Need a website that feels worth paying for?</span><h2>Tell RIID what you’re building.</h2><a class="button light" href="/start/">Start a project ↗</a></section>
</main>
''' + footer()


def about_page():
    return head('About — RIID','RIID is a Nigerian digital studio creating premium websites and digital experiences for ambitious businesses.','/about/','#2b7fff') + nav('About') + f'''
<main>
<section class="page-hero about-hero reveal"><span class="eyebrow"><i></i> About RIID</span><h1>Small studio.<br><em>Serious standards.</em></h1><p>RIID exists to help good businesses stop looking ordinary online.</p></section>
<section class="about-editorial section reveal"><div class="about-big">We care about the details customers notice — and the ones they don’t.</div><div class="about-copy"><p>A website can be the first office, showroom, salesperson or proof of credibility a customer sees. RIID treats it that way.</p><p>Our approach is intentionally focused: understand the business, create a distinct visual direction, build the experience properly, and make the next action obvious.</p></div></section>
<section class="principles section"><div class="section-heading reveal"><div><span class="eyebrow"><i></i> Principles</span><h2>How we think about the work.</h2></div></div><div class="principle-grid"><article class="reveal"><span>01</span><h3>Different business, different website.</h3><p>We do not believe twelve industries should look like twelve recoloured versions of the same layout.</p></article><article class="reveal"><span>02</span><h3>Clarity beats decoration.</h3><p>Beautiful work still has to help people understand, trust and act.</p></article><article class="reveal"><span>03</span><h3>Nigerian context matters.</h3><p>The language, imagery, devices, customer habits and conversion paths should feel relevant here.</p></article><article class="reveal"><span>04</span><h3>Premium does not mean noisy.</h3><p>Confidence comes from typography, hierarchy, photography, motion and restraint — not from adding more effects.</p></article></div></section>
<section class="nigeria-section reveal"><div><span class="eyebrow light"><i></i> RIID</span><h2>Built in Nigeria.<br><em>Thinking beyond it.</em></h2></div><p>We design for Nigerian businesses that want to look credible at home and competitive anywhere their customers find them.</p><div class="ng-cities"><span>Strategy</span><span>Design</span><span>Development</span><span>Growth</span></div></section>
<section class="cta-section reveal"><span>Ready when you are.</span><h2>Bring the business. We’ll shape the digital experience.</h2><a class="button light" href="/start/">Start a project ↗</a></section>
</main>
''' + footer()


def contact_page(start=False):
    label='Start a project' if start else 'Contact'
    headline='Tell us what you’re building.' if start else 'A good project starts with a real conversation.'
    sub='Give RIID the basics. We’ll turn your answers into a pre-filled WhatsApp enquiry so the conversation starts with context.' if start else 'The fastest way to reach RIID is WhatsApp. If you already know what you need, use the project form and send everything in one message.'
    active=''
    return head(f'{label} — RIID',sub,'/start/' if start else '/contact/','#2b7fff') + nav(active) + f'''
<main>
<section class="contact-shell">
  <div class="contact-copy reveal"><span class="eyebrow"><i></i> {label}</span><h1>{headline}</h1><p>{sub}</p><a class="direct-whatsapp" href="https://wa.me/{PHONE_WA}?text=Hi%20RIID%2C%20I%27d%20like%20to%20discuss%20a%20website%20project." target="_blank" rel="noopener"><span>WhatsApp directly</span><strong>{PHONE_DISPLAY}</strong><b>↗</b></a><div class="contact-note"><span>Lagos, Nigeria</span><span>Available for projects across Nigeria</span></div></div>
  <form class="project-form reveal delay-1" data-whatsapp-form>
    <div class="form-row"><label>Your name<input required name="name" autocomplete="name" placeholder="Your name"></label><label>Business name<input required name="business" placeholder="Your business"></label></div>
    <label>What are we building?<select required name="service"><option value="">Select a service</option><option>Business website</option><option>E-commerce website</option><option>Website redesign</option><option>Landing page / lead funnel</option><option>Other digital project</option></select></label>
    <div class="form-row"><label>Budget range<select required name="budget"><option value="">Select range</option><option>₦200k – ₦350k</option><option>₦350k – ₦600k</option><option>₦600k – ₦1m</option><option>₦1m+</option><option>Not sure yet</option></select></label><label>Ideal timeline<select required name="timeline"><option value="">Select timeline</option><option>As soon as possible</option><option>2–4 weeks</option><option>1–2 months</option><option>Flexible</option></select></label></div>
    <label>Tell us about the business<textarea required name="brief" rows="6" placeholder="What does the business do, and what should the website help you achieve?"></textarea></label>
    <button class="button primary form-submit" type="submit">Continue on WhatsApp ↗</button>
    <p class="form-note">No payment is taken here. Your answers are only used to prepare your WhatsApp enquiry.</p>
  </form>
</section>
</main>
''' + footer()


def project_page(p, idx):
    related=[q for q in projects if q['slug']!=p['slug']][:3]
    related_cards=''.join(project_card(q,'normal') for q in related)
    features=''.join(f'<li>{f}</li>' for f in p['features'])
    return head(f"{p['name']} — RIID Concept Project",p['summary'],f"/work/{p['slug']}/",p['accent']) + nav('Work') + f'''
<main>
<section class="project-hero" style="--accent:{p['accent']}">
  <div class="project-hero-copy reveal"><a class="back-link" href="/work/">← All projects</a><span class="eyebrow"><i></i> Concept project · {p['industry']}</span><h1>{p['name']}</h1><p>{p['tagline']}</p><a class="button primary accent-btn" href="/start/">Start a similar project ↗</a></div>
  <div class="project-hero-art reveal delay-1"><div class="browser-frame tilt"><div class="browser-bar"><span></span><span></span><span></span><b>{p['name']}</b></div><img src="{p['image']}" alt="{html.escape(p['name'])} website concept mockup"></div></div>
</section>
<section class="project-overview section"><div class="project-index">0{idx+1}</div><div class="project-overview-main reveal"><span class="eyebrow"><i></i> The direction</span><h2>{p['summary']}</h2></div><div class="project-overview-side reveal"><h3>Art direction</h3><p>{p['visual']}</p><h3>Designed around</h3><ul>{features}</ul></div></section>
<section class="project-canvas reveal" style="--accent:{p['accent']}"><div class="project-canvas-head"><span>Desktop concept</span><span>RIID · {p['industry']}</span></div><img src="{p['image']}" alt="Full website concept presentation for {html.escape(p['name'])}"></section>
<section class="project-value section"><div class="section-heading reveal"><div><span class="eyebrow"><i></i> Business value</span><h2>The design is not the end goal.<br><em>The customer journey is.</em></h2></div></div><div class="value-grid"><article class="reveal"><span>01</span><h3>Look credible immediately</h3><p>A stronger first impression helps the business feel established before a call or WhatsApp conversation starts.</p></article><article class="reveal"><span>02</span><h3>Make the offer easier to understand</h3><p>Clear hierarchy helps visitors understand what the business does, who it is for and why they should care.</p></article><article class="reveal"><span>03</span><h3>Move visitors to action</h3><p>CTAs, forms and WhatsApp handoff are positioned around the customer’s next logical step.</p></article></div></section>
<section class="related section"><div class="section-heading reveal"><div><span class="eyebrow"><i></i> More work</span><h2>Different industries. Different directions.</h2></div><a class="text-link" href="/work/">View all work ↗</a></div><div class="featured-grid">{related_cards}</div></section>
<section class="cta-section compact reveal"><span>Want this level of thought for your business?</span><h2>Let’s create something that belongs to you.</h2><a class="button light" href="/start/">Start a project ↗</a></section>
</main>
''' + footer()

# Write pages
(ROOT/'index.html').write_text(home_page(), encoding='utf-8')
for folder,content in [
    ('work',work_page()),('services',services_page()),('about',about_page()),('contact',contact_page(False)),('start',contact_page(True))
]:
    d=ROOT/folder; d.mkdir(parents=True, exist_ok=True); (d/'index.html').write_text(content, encoding='utf-8')
for i,p in enumerate(projects):
    d=ROOT/'work'/p['slug']; d.mkdir(parents=True, exist_ok=True); (d/'index.html').write_text(project_page(p,i), encoding='utf-8')

# JSON project data
(ROOT/'assets').mkdir(exist_ok=True)
(ROOT/'assets'/'projects.json').write_text(json.dumps(projects, indent=2), encoding='utf-8')

# Sitemap
urls=['/','/work/','/services/','/about/','/contact/','/start/']+[f"/work/{p['slug']}/" for p in projects]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(f'<url><loc>https://riid.ng{u}</loc></url>' for u in urls)+'\n</urlset>',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://riid.ng/sitemap.xml\n',encoding='utf-8')
print('Generated', len(urls), 'pages/routes')
