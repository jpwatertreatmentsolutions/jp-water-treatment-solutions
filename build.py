import json,os
ASSET_V="20261030"
from urllib.parse import quote
BASE="https://YOUR-DOMAIN.com"   # replace before launch
NAME="JP Water Treatment Solutions"
PHONE_D="+91 99948 85701";PHONE_T="+919994885701";WA="919994885701"
ADDR="CBM College Road, Bharathi Nagar, Kovaipudur, Coimbatore, Tamil Nadu 641042"
GBP="https://share.google/9LptjNaivblmGxZyX"
EMAIL="jpwatersolution04@gmail.com"
TEAM=[("Salaman Raj S","Managing Director","+91 99948 85701","+919994885701"),("Alexander S","Manager","+91 98430 10518","+919843010518")]
TEAMCARDS="".join(f'<div class="card person"><span class="avatar" aria-hidden="true">{n[0]}</span><div><h3>{n}</h3><p class="role">{r}</p><p><a href="tel:{t}" data-track="call_click">{d}</a></p><p><a class="btn line" href="tel:{t}" data-track="call_click" aria-label="Call {n}, {r}">Call {n.split()[0]}</a></p></div></div>' for n,r,d,t in TEAM)
TEAMLINES="".join(f'<p><strong>{n}</strong>, {r}<br><a href="tel:{t}" data-track="call_click">{d}</a></p>' for n,r,d,t in TEAM)
IG="https://www.instagram.com/jp_water_treatment_solutions"
FB="https://www.facebook.com/share/1F3FQxB7rf/"
EMBED="https://www.google.com/maps?q=JP+Water+Treatment+Solutions,+CBM+College+Road,+Kovaipudur,+Coimbatore+641042&output=embed"
MAPS="https://www.google.com/maps/search/?api=1&query=JP+Water+Treatment+Solutions+Kovaipudur+Coimbatore"
IM={"stp":("projects/project-stp",800,533),"ro":("projects/project-ro",800,533),"etp":("projects/project-pressure-vessel",800,533),"soft":("projects/project-softener",800,533),"amc":("amc_maintenance",451,206),"op":("projects/project-rooftop-vessels",800,533),"ind":("industrial_water_treatment",469,206)}
def pic(k,alt,lazy=True,sizes="(max-width:820px) 100vw, 520px"):
    f,w,h=IM[k];l=' loading="lazy" decoding="async"' if lazy else ''
    if f.startswith("projects/"):
        foc=' data-focus="top"' if "pressure-vessel" in f else ''
        return f'<picture><source type="image/webp" srcset="/public/images/{f}-800.webp 800w, /public/images/{f}-1536.webp 1536w" sizes="{sizes}"><img src="/public/images/{f}-800.jpg" srcset="/public/images/{f}-800.jpg 800w, /public/images/{f}-1536.jpg 1536w" sizes="{sizes}" width="{w}" height="{h}"{foc} alt="{alt}"{l}></picture>'
    return f'<picture><source type="image/webp" srcset="/public/images/{f}.webp"><img src="/public/images/{f}.jpg" width="{w}" height="{h}" alt="{alt}"{l}></picture>'
AREAS=[{"@type":"State","name":"Tamil Nadu"},{"@type":"State","name":"Kerala"},{"@type":"City","name":"Bengaluru"}]
S=[
dict(k="stp",id="stp",q="stp",h="STP Plant Manufacturing and Installation in Tamil Nadu",nm="STP Manufacturing & Installation",
 alt="Sewage treatment plant room with an electrical control panel, a blower and pumps",
 card="We manufacture, install and commission sewage treatment plants, including for new apartments, and can support plant operation.",anc="STP plant manufacturing, installation and operation",
 intro="We manufacture and install sewage treatment plants (STP), including installations for newly constructed apartments. From our base in Coimbatore we handle STP plant installation in Tamil Nadu and serve customers in Kerala and Bengaluru. Each plant is planned around your project, and installation is followed by commissioning and handover.",
 prob=["Sewage treatment for new apartments and buildings","Choosing between an iron-structure plant and civil tanks","Meeting local discharge and reuse requirements"],
 apps=["Newly constructed apartments","Gated communities","Hotels and hospitals","Schools, colleges and offices","Commercial complexes"],
 svch="What an STP installation can include",
 svc=["Iron structures or civil tanks, depending on the project","Motors, pumps and diffusers","Pipelines","Electrical and plumbing connections","Commissioning and handover"],
 note="The exact scope depends on your project requirements and is confirmed in the agreed quotation.",
 info=["Type of building and number of occupants or flats","Approximate daily sewage volume","Preference for civil tanks or iron structure, if any","Available space","Site location"]),
dict(k="op",id="stp-operation",q="stp-operation",h="STP Plant Operation, Manpower and Training",nm="STP Operation, Manpower & Training",nocard=True,
 alt="Two large blue pressure vessels with pipework on a rooftop plant, with hills in the background",
 card="Operator manpower, guidance for your own operators and staff training.",anc="STP operation, manpower and training",
 intro="A treatment plant needs regular attention to work well. Where required, we provide manpower to operate treatment plants, guide the operators you appoint and train your staff. Operation, manpower and training are separate from plant installation and are agreed separately according to your needs.",
 prob=["No trained person available to run the plant","Operators who need guidance on routine procedures","Staff who need training in basic plant care"],
 apps=["Apartment and community STPs","Hotels, hospitals and institutions","Commercial buildings"],
 svch="Ways we can help",
 svc=["We provide manpower to operate the plant","We guide operators appointed by the customer","We train the customer's staff when required"],
 note="Scope, number of operators, duration and charges are agreed separately from the installation.",
 info=["Type and capacity of the plant","Whether you need our operators, guidance for yours, or staff training","Working hours or shifts needed","Site location"]),
dict(k="ro",id="ro-plant",q="ro",h="RO Plant Installation and Drinking-Water Treatment",nm="RO Plant & Drinking-Water Treatment",
 alt="RO plant with membrane pressure vessels on a steel rack and white pipework",
 card="RO plant solutions and installation for drinking water, with manpower or maintenance support where agreed.",anc="RO plant installation and drinking-water treatment",
 intro="Reverse osmosis (RO) reduces dissolved salts and many impurities by passing water through fine membranes. We provide RO plant solutions for drinking-water treatment, from RO plant installation to operational manpower or maintenance support where required and agreed. If you need an RO plant in Coimbatore or elsewhere in Tamil Nadu, Kerala or Bengaluru, share your water details and requirement.",
 prob=["High dissolved salts (TDS) or unpleasant taste in borewell water","Need for safe, consistent drinking water","Scale build-up in equipment from salty water"],
 apps=["Apartments and residential communities","Hospitals and institutions","Factories and process units","Commercial kitchens and buildings"],
 svch="Installation, operation and maintenance",
 svc="We can install the RO plant and, where required and agreed, provide operational manpower or maintenance support (RO plant installation and maintenance).",
 info=["Water source (borewell, tank, municipal) and a water test report if available","Required daily output","Intended use: drinking, process or other","Space and power available","Site location"]),
dict(k="etp",id="etp",q="etp",h="ETP and Industrial Wastewater Treatment",nm="ETP & Industrial Wastewater Treatment",
 alt="Person working at a fibreglass pressure vessel with pipework and a control box at an outdoor plant",
 card="Effluent treatment plant solutions and wastewater management for factories and other businesses.",anc="ETP and industrial wastewater treatment",
 intro="We provide effluent treatment plant (ETP) solutions and industrial wastewater management for factories and other businesses. The treatment arrangement depends on the characteristics of your wastewater and the requirements of the project, so we begin by understanding your effluent.",
 prob=["Process wastewater that cannot be discharged untreated","Meeting discharge requirements (these vary, so confirm them with the relevant authority)","Reusing treated water to reduce water demand"],
 apps=["Factories and manufacturing units","Textile and dyeing units","Food processing units","Laundries","Other businesses that generate wastewater"],
 svch="Installation and maintenance",svc="We can discuss ETP plant design, installation and ongoing maintenance support based on your effluent and project needs.",
 info=["Industry and process that generates the effluent","Approximate daily effluent quantity","Effluent test report, if available","Discharge or reuse goal","Available space and site location"]),
dict(k="soft",id="water-softener",q="softener",h="Water Softener and Hard-Water Treatment",nm="Water Softener Systems",
 alt="Large blue water softener pressure vessel with pipework on a rooftop plant area",
 card="Softening solutions for borewell and hard water, chosen for your water quality and requirement.",anc="Water softener and hard-water treatment",
 intro="Borewell and other hard water contains calcium and magnesium that cause scale. We provide suitable water-softening solutions depending on your water quality and requirements. A water softener can reduce hardness and scale formation in pipes, heaters, boilers and appliances. It is a water treatment measure and not a medical treatment.",
 prob=["Scale on pipes, heaters, boilers and fittings","Reduced efficiency of equipment","Stains on fixtures and soap scum"],
 apps=["Apartments and villas","Hotels and hospitals","Laundries","Boiler and cooling systems","Food and beverage units"],
 svch="Installation and maintenance",svc="Contact us to discuss the right softener for your water, along with installation and regular servicing.",
 info=["Water hardness level, if known","Daily water usage or flow rate","Number of users or connected equipment","Space available","Site location"]),
dict(k="amc",id="amc",q="amc",h="AMC and Maintenance Services for Water Treatment Plants",nm="AMC & Preventive Maintenance",
 alt="Illustration of a technician operating the control panel of a water treatment plant",
 card="Annual maintenance contracts with scheduled visits, plant servicing and inspection reports.",anc="AMC and maintenance services",
 intro="Our annual maintenance contract (AMC) services keep treatment plants working through scheduled visits, either monthly or once every 15 days according to the agreed plan. Whether you need STP operation and AMC services or maintenance for another water treatment plant, tell us about your plant and we will explain the options.",
 prob=["Unplanned breakdowns and downtime","Sludge build-up and odour problems","Delayed servicing of pumps and tanks","No written record of the plant's condition"],
 apps=["Existing STP plants","RO plants","ETP and other treatment plants","Water softener systems"],
 svch="What maintenance can include",
 svc=["Checking the condition of pumps and tanks","Monitoring sludge accumulation","Inspecting odour-control measures","Supplying required chemicals, where included in the contract","Servicing the plant","Detailed inspection reports"],
 note="Manpower, chemical supplies, spare parts, repair work and visit frequency depend on the agreed AMC scope.",
 info=["Type and capacity of the plant","Preferred visit frequency (monthly or every 15 days)","Whether you expect chemicals and manpower to be included","Current problems or recent breakdowns","Site location"]),
dict(k="ind",id="industrial-water-treatment",q="industrial",h="Industrial Water Treatment Solutions",nm="Industrial Water Treatment",
 alt="Industrial water treatment equipment with filter vessels, a steel tank and membrane skid",
 card="Industrial water purification and treatment systems built around your process.",anc="Industrial water treatment solutions",
 intro="Industrial units rely on water of the right quality for processing, boilers, cooling and cleaning. Industrial water treatment solutions often combine several steps, such as filtration, softening and reverse osmosis. We plan the system around your process and water source, from our base in Coimbatore for customers across Tamil Nadu, Kerala and Bengaluru.",
 prob=["Unstable or poor raw water quality","Scale and corrosion in equipment","Strict water quality needs in production","Handling and treating process wastewater"],
 apps=["Manufacturing units","Textile and engineering units","Food processing units","Boiler and cooling systems"],
 svch="Installation and maintenance",svc="Discuss system design, installation and maintenance support for your unit.",
 info=["Type of industry and process","Water source and quality","Required quantity and quality of treated water","Current problems","Site location"]),
]
FAQ=[("Which water treatment services do you offer?","We offer STP manufacturing and installation, STP operation, manpower and training, AMC and maintenance, RO plants, water softener systems, ETP and industrial wastewater treatment, and industrial water treatment."),
("Do you manufacture and install STP plants?","Yes. We manufacture and install sewage treatment plants, including for newly constructed apartments. Depending on the project, this can include iron structures or civil tanks, motors, pumps, diffusers, pipelines and electrical and plumbing connections, followed by commissioning and handover."),
("Can you operate the plant or train our staff?","Where required, we can provide manpower to operate the plant, guide operators you appoint and train your staff. These services are agreed separately from installation."),
("What does an AMC include?","Our AMC provides scheduled visits, monthly or once every 15 days according to the agreed plan, with checks on pumps and tanks, sludge monitoring, odour-control inspection, plant servicing and inspection reports. Manpower, chemicals, spare parts, repairs and visit frequency depend on the agreed scope."),
("Which areas do you serve?","We are based in Coimbatore, Tamil Nadu, and provide services across Tamil Nadu, Kerala and Bengaluru, Karnataka. Share your site location and we will discuss your requirement."),
("What is the difference between an STP and an ETP?","An STP treats sewage from buildings such as apartments, hotels and offices. An ETP treats wastewater produced by industrial processes. The right choice depends on where the wastewater comes from."),
("What information do I need for a quote?","Share the type of plant you need, your water source or wastewater type, approximate daily volume and site location. A water or effluent test report helps, but is not required to start the conversation.")]
NAV=NAV=[("/","Home"),("/services/","Services"),("/about-us/","About Us"),("/contact-us/","Contact Us")]
OG={"/":"og-share.jpg","/services/":"og-services.jpg","/about-us/":"og-about.jpg","/contact-us/":"og-contact.jpg"}
def head(t,d,path,extra="",preload="",robots="index, follow"):
    url=BASE+path
    ogimg=OG.get(path,"og-share.jpg")
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0a2342"><script>document.documentElement.className+=" js"</script>
<meta property="og:type" content="website"><meta property="og:site_name" content="{NAME}"><meta property="og:locale" content="en_IN">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/public/images/{ogimg}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<!-- Google Search Console: add the HTML-tag verification meta here, e.g. <meta name="google-site-verification" content="YOUR_CODE"> -->
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png"><link rel="icon" href="/assets/icon-192.png" sizes="192x192" type="image/png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Plus+Jakarta+Sans:wght@700;800&display=swap">
{preload}<link rel="stylesheet" href="/assets/style.css?v={ASSET_V}">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''
def ld(o):return '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>\n'
LB={"@context":"https://schema.org","@type":"LocalBusiness","@id":BASE+"/#business","name":NAME,"url":BASE+"/",
 "description":"Coimbatore-based water treatment company serving Tamil Nadu, Kerala and Bengaluru: STP, RO plants, ETP, water softeners, AMC and industrial water treatment.",
 "telephone":PHONE_T,"image":BASE+"/public/images/og-share.jpg","hasMap":MAPS,"email":EMAIL,"sameAs":[GBP,IG,FB],"logo":BASE+"/assets/logo-512.png",
 "address":{"@type":"PostalAddress","streetAddress":"CBM College Road, Bharathi Nagar, Kovaipudur","addressLocality":"Coimbatore","addressRegion":"Tamil Nadu","postalCode":"641042","addressCountry":"IN"},
 "areaServed":AREAS,"foundingDate":"2018","employee":[{"@type":"Person","name":n,"jobTitle":r,"telephone":t} for n,r,d,t in TEAM]}
def crumb(name,path):
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":name,"item":BASE+path}]})
def top(cur):
    subs="".join(f'<li><a href="/services/#{s["id"]}">{s["nm"]}</a></li>' for s in S)
    items=""
    for hh,n in NAV:
        ca=' aria-current="page"' if hh==cur else ''
        items+=(f'<li class="has-sub"><a href="{hh}"{ca}>{n}</a><button type="button" class="sub-toggle" aria-expanded="false" aria-label="Show services menu">&#9662;</button><ul class="sub">{subs}</ul></li>' if hh=="/services/" else f'<li><a href="{hh}"{ca}>{n}</a></li>')
    return f'''<div class="topbar" role="region" aria-label="Contact details"><div class="wrap"><span>Kovaipudur, Coimbatore, Tamil Nadu</span><span><a href="tel:{PHONE_T}" data-track="call_click">{PHONE_D}</a> &middot; <a href="https://wa.me/{WA}" target="_blank" rel="noopener" data-track="whatsapp_click">WhatsApp</a></span></div></div>
<header class="site"><div class="wrap nav"><a class="brand" href="/"><img src="/assets/logo-96.webp" width="48" height="48" alt="" decoding="async">{NAME}</a>
<button id="menu" aria-label="Toggle menu" aria-expanded="false" aria-controls="links">Menu</button>
<nav class="nav" aria-label="Main" style="height:auto"><ul id="links">{items}</ul></nav>
<a class="btn hq" href="/contact-us/#quote" data-track="get_quote_click">Get a Quote</a></div></header>
<main id="main">
'''
def cbform(src,idp):
    return f'<form class="cb-form" data-src="{src}" novalidate><label for="{idp}-n">Name<input id="{idp}-n" name="name" autocomplete="name" required aria-required="true"></label><label for="{idp}-p">Phone<input id="{idp}-p" name="phone" type="tel" autocomplete="tel" required aria-required="true"></label><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn" type="submit">Call me back</button><div class="cb-msg" role="status" aria-live="polite"></div></form>'
CBHERO='<aside class="cb-card" aria-labelledby="cb-hero-h"><h2 id="cb-hero-h">Request a call back</h2><p>Leave your number and we will call you.</p>'+cbform("hero","cbh")+'</aside>'
CBFOOT='<div class="cb-strip"><div class="wrap cb-in"><div><h2 id="cb-foot-h">Request a call back</h2><p>Leave your name and number and we will call you back.</p></div>'+cbform("footer","cbf")+'</div></div>'
FOOT=f'''</main>
<footer>{CBFOOT}<div class="wrap cols">
<div><img src="/assets/logo-192.webp" width="96" height="96" alt="JP Water Treatment Solutions logo" loading="lazy" decoding="async" style="margin-bottom:12px"><h2>{NAME}</h2><p>Water and wastewater treatment: plant manufacturing, installation, operation, staff training and maintenance.</p><p><a href="{GBP}" target="_blank" rel="noopener">Find us on Google</a></p><div class="soc"><a href="{FB}" target="_blank" rel="noopener" aria-label="JP Water Treatment Solutions on Facebook" data-track="social_click"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 8V6.500c0-.7.3-1 1-1h2V2h-3a4 4 0 0 0-4 4v2H7v3.500h3V22h4V11.500h3l.5-3.500H14z"/></svg></a><a href="{IG}" target="_blank" rel="noopener" aria-label="JP Water Treatment Solutions on Instagram" data-track="social_click"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.500" cy="6.500" r="1" fill="currentColor" stroke="none"/></svg></a><a href="{GBP}" target="_blank" rel="noopener" aria-label="JP Water Treatment Solutions on Google" data-track="gbp_click"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.500"/></svg></a></div></div>
<div><h2>Useful Links</h2><ul>{"".join(f'<li><a href="{h}">{n}</a></li>' for h,n in NAV)}<li><a href="/privacy-policy/">Privacy Policy</a></li></ul></div>
<div><h2>Our Services</h2><ul>{"".join(f'<li><a href="/services/#{s["id"]}">{s["nm"]}</a></li>' for s in S)}</ul></div>
<div><h2>Get in Touch</h2><address>CBM College Road, Bharathi Nagar,<br>Kovaipudur, Coimbatore,<br>Tamil Nadu 641042</address><p style="margin:.6em 0">Serving Tamil Nadu, Kerala &amp; Bengaluru</p>
<p><a href="tel:{PHONE_T}" data-track="call_click">{PHONE_D}</a> (Managing Director)<br><a href="tel:+919843010518" data-track="call_click">+91 98430 10518</a> (Manager)<br><a href="mailto:{EMAIL}" data-track="email_click">{EMAIL}</a><br><a href="https://wa.me/{WA}" target="_blank" rel="noopener" data-track="whatsapp_click">WhatsApp</a><br><a href="{MAPS}" target="_blank" rel="noopener">View on Google Maps</a></p></div>
</div><div class="wrap" style="margin-top:26px;font-size:.85rem;opacity:.9">&copy; 2026 {NAME} &middot; <button type="button" class="linklike" id="cookie-settings" hidden>Cookie settings</button></div><div class="consent" id="consent" role="dialog" aria-label="Cookie consent" hidden><p>We would like to use analytics cookies to understand how visitors use this site and improve it. See our <a href="/privacy-policy/">Privacy Policy</a>.</p><div class="btns"><button type="button" class="btn" id="consent-yes">Accept</button><button type="button" class="btn ghost" id="consent-no">Decline</button></div></div></footer>
<div role="region" aria-label="Page tools"><button type="button" class="totop" id="totop" aria-label="Back to top">&uarr;</button></div>
<div class="mbar" role="navigation" aria-label="Quick contact"><a class="m-call" href="tel:{PHONE_T}" data-track="call_click">Call</a><a class="m-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" data-track="whatsapp_click">WhatsApp</a><a class="m-q" href="/contact-us/#quote" data-track="get_quote_click">Get a Quote</a><a class="m-ig" href="{IG}" target="_blank" rel="noopener" aria-label="Follow JP Water Treatment Solutions on Instagram" data-track="social_click"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.200" cy="6.800" r="1.100" fill="#fff" stroke="none"/></svg></a></div>
<div class="float" role="region" aria-label="Quick contact icons"><a class="call" href="tel:{PHONE_T}" aria-label="Call {NAME}" data-track="call_click"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.600 10.800a15 15 0 0 0 6.600 6.600l2.200-2.200c.3-.3.7-.4 1-.2 1.100.4 2.300.6 3.600.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.500c.6 0 1 .4 1 1 0 1.300.2 2.500.6 3.600.1.300 0 .7-.2 1z"/></svg></a>
<a class="wa" href="https://wa.me/{WA}?text=Hello%20JP%20Water%20Treatment%20Solutions%2C%20I%20need%20a%20quote." target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-track="whatsapp_click"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.600 15.100L2 22l5-1.300A10 10 0 1 0 12 2zm5.200 14.100c-.2.600-1.300 1.200-1.800 1.200-.5.100-1 .2-3.300-.7-2.800-1.200-4.600-4-4.700-4.200-.1-.2-1.100-1.500-1.100-2.800s.7-2 1-2.300c.2-.3.500-.3.700-.3h.5c.2 0 .4 0 .6.500l.8 2c.1.2.1.3 0 .5l-.3.400-.4.400c-.1.200-.3.300-.1.600.2.300.8 1.300 1.700 2.100 1.200 1 2.100 1.300 2.400 1.500.3.100.5.100.7-.1l.9-1.100c.2-.3.4-.2.7-.1l1.900.9c.3.100.5.200.5.300.1.200.1.800-.1 1.300z"/></svg></a><a class="ig" href="{IG}" target="_blank" rel="noopener" aria-label="Follow JP Water Treatment Solutions on Instagram" data-track="social_click"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.200" cy="6.800" r="1.100" fill="#fff" stroke="none"/></svg></a></div>
<script src="/assets/site.js?v={ASSET_V}" defer></script>
</body></html>
'''
def ctas(extra=""):
    return f'<div class="btns"><a class="btn" href="/contact-us/#quote" data-track="get_quote_click">Get a Quote</a><a class="btn ghost" href="tel:{PHONE_T}" data-track="call_click">Call Now</a><a class="btn ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener" data-track="whatsapp_click">WhatsApp Us</a></div>'
def band(h,p):return f'<div class="cta"><div class="wrap"><h2>{h}</h2><p>{p}</p>{ctas()}</div></div>\n'
def w(path,html):
    os.makedirs("out/"+path,exist_ok=True);open("out/"+path+"/index.html" if path else "out/index.html","w").write(html)
PAGES={}
TICK=["STP manufacturing &amp; installation","STP operation","Manpower &amp; staff training","AMC &amp; maintenance","RO plants","Water softeners","ETP &amp; industrial wastewater","Industrial water treatment"]
# HOME
t="Water Treatment Company in Tamil Nadu | JP Water Treatment"
d="Coimbatore-based water treatment company serving Tamil Nadu, Kerala and Bengaluru: STP, RO, ETP, softeners and AMC, from manufacturing to maintenance."
PAGES["/"]=(t,d,"Water Treatment Solutions Across Tamil Nadu","water treatment company Tamil Nadu; services in Coimbatore; Kerala, Bengaluru")
pre='<link rel="preload" as="image" href="/public/images/projects/project-rooftop-vessels-1536.webp" type="image/webp" imagesrcset="/public/images/projects/project-rooftop-vessels-800.webp 800w, /public/images/projects/project-rooftop-vessels-1536.webp 1536w" imagesizes="100vw" fetchpriority="high">\n'
BY={x["id"]:x for x in S}
def pcard(i):
    x=BY[i];return f'<article class="card pc rv">{pic(x["k"],x["alt"],sizes="(max-width:700px) 100vw, 360px")}<div class="body"><h3>{x["nm"]}</h3><p>{x["card"]}</p><a class="more" href="/services/#{x["id"]}">{x["anc"]} &rarr;</a></div></article>\n'
SL=[("STP manufacturing and installation","stp"),("STP operation, manpower and staff training","stp-operation"),("AMC with scheduled visits and inspection reports","amc"),("RO plant installation and drinking-water treatment","ro-plant"),("Water softener and hard-water treatment","water-softener"),("ETP and industrial wastewater management","etp"),("Industrial water treatment solutions","industrial-water-treatment")]
h=head(t,d,"/",ld(LB)+ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}),pre)+top("/")
ICO={"fac":"M3 21h18M5 21V8l5 3V8l5 3V5h4v16","pin":"M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11zM12 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4","tool":"M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z","tel":"M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"}
ICO["mail"]="M4 6h16v12H4zM4 7l8 6 8-6"
ICO["globe"]="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"
ico=lambda k:f'<div class="ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="{ICO[k]}"/></svg></div>'
def card(sid):
    x=next(v for v in S if v["id"]==sid)
    return f'<article class="card pc">{pic(x["k"],x["alt"],sizes="(max-width:700px) 100vw, 360px")}<div class="body"><h3>{x["nm"]}</h3><p>{x["card"]}</p><a class="more" href="/services/#{x["id"]}">{x["anc"]} &rarr;</a></div></article>'
panel=lambda ids:'<div class="cards">'+"".join(card(i) for i in ids)+'</div>'
ABOUTPIC=pic("stp","Sewage treatment plant room with an electrical control panel, a blower and pumps",sizes="(max-width:820px) 100vw, 520px")
h+=f'''<section class="hero" id="top"><picture><source type="image/webp" srcset="/public/images/projects/project-rooftop-vessels-800.webp 800w, /public/images/projects/project-rooftop-vessels-1536.webp 1536w" sizes="100vw"><img src="/public/images/projects/project-rooftop-vessels-1536.jpg" width="1536" height="1024" fetchpriority="high" alt="Two large blue water treatment pressure vessels with pipework on a rooftop plant, with hills in the background"></picture>
<div class="wrap herogrid"><div class="herotxt"><span class="tag">Based in Coimbatore, Tamil Nadu</span><h1>Water Treatment Solutions Across Tamil Nadu</h1>
<p>Complete water treatment solutions, from plant manufacturing and installation to operation, staff training, and ongoing maintenance. Serving customers across Tamil Nadu, Kerala, and Bengaluru.</p>{ctas()}</div></div>
<svg class="wave" viewBox="0 0 1200 54" preserveAspectRatio="none" aria-hidden="true"><path d="M0 27Q150 0 300 27T600 27T900 27T1200 27V54H0z"/></svg></section>
<section id="about"><div class="wrap two" style="align-items:center"><div><span class="eyebrow">About the company</span><h2>A water treatment company based in Coimbatore</h2>
<p class="lead">JP Water Treatment Solutions is based in Kovaipudur, Coimbatore, and provides water treatment services in Coimbatore and across Tamil Nadu, Kerala and Bengaluru. We were established in 2018 and have completed more than 100 projects.</p>
<ul class="checks"><li>Manufacture and installation of sewage treatment plants, including for new apartments</li><li>Plant operation, manpower and staff training, agreed separately</li><li>AMC with scheduled visits, servicing and inspection reports</li><li>RO, water softener, ETP and industrial water treatment solutions</li></ul>
<p><a class="btn" href="/about-us/" aria-label="About JP Water Treatment Solutions">Learn More About Us</a></p></div>
<div class="about-img">{ABOUTPIC}<div class="badge"><b>2018</b><span>Established</span></div></div></div></section>
<section class="alt" id="solutions"><div class="wrap"><span class="eyebrow">Our solutions</span><h2>Water and wastewater treatment</h2><p class="lead">Choose a category to see what we provide. Each solution links to the full details on our services page.</p>
<div class="tabs" role="tablist" aria-label="Solution categories"><button type="button" role="tab" id="tb-water" aria-controls="tp-water" aria-selected="true">Water Treatment</button><button type="button" role="tab" id="tb-waste" aria-controls="tp-waste" aria-selected="false">Wastewater Treatment</button><button type="button" role="tab" id="tb-om" aria-controls="tp-om" aria-selected="false">Operation &amp; Maintenance</button></div>
<div class="tabpanel" id="tp-water" role="tabpanel" aria-labelledby="tb-water">{panel(["ro-plant","water-softener","industrial-water-treatment"])}</div>
<div class="tabpanel" id="tp-waste" role="tabpanel" aria-labelledby="tb-waste">{panel(["stp","etp"])}</div>
<div class="tabpanel" id="tp-om" role="tabpanel" aria-labelledby="tb-om">{panel(["stp-operation","amc"])}</div></div></section>
<section id="projects"><div class="wrap"><span class="eyebrow">Our projects</span><h2>A look at our work</h2><p class="lead">Photographs from our projects. Select a photo to view it larger.</p>
<div class="gallery"><figure class="gitem"><a class="gal" href="/public/images/projects/project-stp-1536.jpg" data-cap="Sewage Treatment Plant"><picture><source type="image/webp" srcset="/public/images/projects/project-stp-800.webp"><img src="/public/images/projects/project-stp-800.jpg" width="800" height="533" loading="lazy" decoding="async" alt="Sewage treatment plant room with an electrical control panel, a blower and pumps"></picture></a><figcaption>Sewage Treatment Plant</figcaption></figure><figure class="gitem"><a class="gal" href="/public/images/projects/project-ro-1536.jpg" data-cap="RO Plant"><picture><source type="image/webp" srcset="/public/images/projects/project-ro-800.webp"><img src="/public/images/projects/project-ro-800.jpg" width="800" height="533" loading="lazy" decoding="async" alt="RO plant with membrane pressure vessels on a steel rack and white pipework"></picture></a><figcaption>RO Plant</figcaption></figure><figure class="gitem"><a class="gal" href="/public/images/projects/project-softener-1536.jpg" data-cap="Water Softener"><picture><source type="image/webp" srcset="/public/images/projects/project-softener-800.webp"><img src="/public/images/projects/project-softener-800.jpg" width="800" height="533" loading="lazy" decoding="async" alt="Large blue water softener pressure vessel with pipework on a rooftop plant area"></picture></a><figcaption>Water Softener</figcaption></figure><figure class="gitem"><a class="gal" href="/public/images/projects/project-pressure-vessel-1536.jpg" data-cap="Pressure vessel and pipework"><picture><source type="image/webp" srcset="/public/images/projects/project-pressure-vessel-800.webp"><img src="/public/images/projects/project-pressure-vessel-800.jpg" width="800" height="533" loading="lazy" decoding="async" alt="Person working at a fibreglass pressure vessel with pipework and a control box at an outdoor plant"></picture></a><figcaption>Pressure vessel and pipework</figcaption></figure><figure class="gitem"><a class="gal" href="/public/images/projects/project-rooftop-vessels-1536.jpg" data-cap="Pressure vessels on a rooftop plant"><picture><source type="image/webp" srcset="/public/images/projects/project-rooftop-vessels-800.webp"><img src="/public/images/projects/project-rooftop-vessels-800.jpg" width="800" height="533" loading="lazy" decoding="async" alt="Two large blue pressure vessels with pipework on a rooftop plant, with hills in the background"></picture></a><figcaption>Pressure vessels on a rooftop plant</figcaption></figure></div>
<dialog id="lb" class="lb" aria-label="Project photo"><button type="button" class="lb-x" aria-label="Close photo">&times;</button><img id="lb-img" alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="><p id="lb-cap"></p></dialog></div></section>
<!-- CUSTOMER FEEDBACK: real Google reviews shown as written. To add another review, copy one figure with class "slide" inside the block below and change the name and text. -->
<section class="alt" id="feedback"><div class="wrap"><span class="eyebrow">Customer feedback</span><h2>What our customers say</h2><div class="slider" data-slider><div class="viewport"><div class="slides"><figure class="slide"><blockquote lang="ta">JP Water Treatment Solutions-ன் சேவை மிகவும் அருமையாக இருந்தது. முதல் தொடர்பிலிருந்தே மிகவும் மரியாதையாகவும், பொறுமையாகவும் அனைத்து சந்தேகங்களுக்கும் தெளிவாக விளக்கம் அளித்தார்கள். சரியான நேரத்தில் வந்து இன்ஸ்டாலேஷனை முடித்தவுடன், Water Purifier-ஐ எப்படி பயன்படுத்துவது மற்றும் பராமரிப்பது என்பதையும் விரைவாக சொல்லிக் கொடுத்தார்கள். பொருளின் தரம் மிகவும் சிறப்பாக உள்ளது, தண்ணீரின் சுவையும் தரமும் நல்ல முன்னேற்றம் அடைந்துள்ளது. விற்பனைக்குப் பிறகும் தேவையான உதவியை உடனுக்குடன் வழங்கும் சிறந்த Customer Support உள்ளது. நம்பகமான சேவை, தரமான பொருட்கள், நியாயமான விலை மற்றும் தொழில்முறை அணுகுமுறை ஆகியவற்றால் நான் மிகவும் திருப்தி அடைந்தேன். Water Purifier வாங்க நினைப்பவர்கள் கண்டிப்பாக JP Water Treatment Solutions-ஐ தேர்வு செய்யலாம். மனப்பூர்வமான நன்றி!</blockquote><figcaption><span class="rev-av" aria-hidden="true">C</span><span><b>Chandru Cham</b><span>Google review</span></span><span class="stars" role="img" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span></figcaption></figure><figure class="slide"><blockquote>I had a great experience with JP Water Treatment Solutions. Their team is professional, knowledgeable, and provides excellent support. They offer quality solutions for Water Softener Plants, RO Plants, STP, and WTP systems. The installation was completed on time, and they explained the operation and maintenance clearly. I appreciate their prompt service and commitment to customer satisfaction. I would definitely recommend JP Water Treatment Solutions to anyone looking for reliable water treatment services.</blockquote><figcaption><span class="rev-av" aria-hidden="true">A</span><span><b>A Jibila</b><span>Google review</span></span><span class="stars" role="img" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span></figcaption></figure></div></div><div class="sl-ctrl"><button type="button" class="prev" aria-label="Previous review">&lsaquo;</button><div class="dots"></div><button type="button" class="next" aria-label="Next review">&rsaquo;</button><button type="button" class="pp" aria-label="Pause automatic review rotation" aria-pressed="false">&#10074;&#10074;</button></div></div><p style="text-align:center;margin-top:28px"><a class="btn" href="{GBP}" target="_blank" rel="noopener" data-track="gbp_click">View Customer Reviews</a></p></div></section>
<section id="support"><div class="wrap"><span class="eyebrow">End-to-end support</span><h2>From plant to long-term care</h2><p class="lead">One company for the plant, the people who run it and the maintenance that keeps it working.</p>
<div class="steps"><div class="step"><span class="n" data-n="01" aria-hidden="true"></span><h3>Manufacture &amp; install</h3><p>We manufacture and install sewage treatment plants and provide RO, softener and ETP solutions, followed by commissioning and handover.</p></div>
<div class="step"><span class="n" data-n="02" aria-hidden="true"></span><h3>Operate &amp; train</h3><p>Where required, we provide manpower to operate the plant, guide your operators and train your staff, agreed separately from installation.</p></div>
<div class="step"><span class="n" data-n="03" aria-hidden="true"></span><h3>Maintain with AMC</h3><p>Scheduled visits monthly or every 15 days as agreed, with servicing and detailed inspection reports.</p></div></div><h3 style="margin-top:44px">Where our systems are used</h3><div class="chips"><span>Apartments, including new construction</span><span>Hotels and restaurants</span><span>Hospitals</span><span>Schools and colleges</span><span>Offices and commercial buildings</span><span>Manufacturing units</span><span>Textile units</span><span>Food processing</span></div></div></section>
<section class="ach" id="achievements"><div class="wrap"><span class="eyebrow light">Our achievements</span><h2>Delivering water treatment since 2018</h2>
<div class="statgrid"><div class="stat"><b data-count="100" data-suffix="+">100+</b><span>Projects completed</span></div><div class="stat"><b data-since="2018" data-suffix="+">8+</b><span>Years in water treatment</span></div><div class="stat"><b data-count="7">7</b><span>Service areas</span></div><div class="stat"><b data-count="3">3</b><span>Regions served</span></div></div><div class="ach-cov"><p>Our office is in Kovaipudur, Coimbatore. We provide services across Tamil Nadu, Kerala and Bengaluru, Karnataka.</p><div class="chips"><span>Coimbatore (our base)</span><span>Tamil Nadu</span><span>Kerala</span><span>Bengaluru, Karnataka</span></div></div></div></section>
<section class="alt" id="faq"><div class="wrap"><span class="eyebrow">FAQs</span><h2>Frequently asked questions</h2><div class="faq"><div>
<div class="card"><h3>Still have a question?</h3><p>Call us, message us on WhatsApp or send the quote form.</p><div class="btns" style="margin-top:12px"><a class="btn" href="/contact-us/#quote" data-track="get_quote_click">Get a Quote</a></div></div></div>
<div>{"".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(FAQ))}</div></div></div></section>
'''+band("Need a water treatment solution?","Tell us your requirement and we will get back to you.")+FOOT
w("",h)
SHORT={"stp":"STP Plant","stp-operation":"STP Operation","ro-plant":"RO Plant","etp":"ETP","water-softener":"Softener","amc":"AMC","industrial-water-treatment":"Industrial"}
JUMP='<nav class="jump" aria-label="Jump to a service"><div class="wrap">'+"".join(f'<a href="#{s["id"]}">{SHORT[s["id"]]}</a>' for s in S)+'</div></nav>\n'
# SERVICES
t="STP, RO, ETP & AMC Services in Tamil Nadu | JP Water";d="STP installation, operation and AMC, RO plants, ETP, water softeners and industrial water treatment from Coimbatore, serving Tamil Nadu, Kerala and Bengaluru."
PAGES["/services/"]=(t,d,"Water Treatment Services in Tamil Nadu, Kerala & Bengaluru","STP, RO, ETP, softener, AMC, industrial; Coimbatore base")
sv=[{"@type":"ListItem","position":i+1,"item":{"@type":"Service","name":s["h"],"serviceType":s["nm"],"url":BASE+"/services/#"+s["id"],"provider":{"@id":BASE+"/#business"},"areaServed":AREAS}} for i,s in enumerate(S)]
h=head(t,d,"/services/",ld(LB)+crumb("Services","/services/")+ld({"@context":"https://schema.org","@type":"ItemList","itemListElement":sv}))+top("/services/")
h+='<div class="pagehead ph-services"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Services</nav><h1>Water Treatment Services in Tamil Nadu, Kerala &amp; Bengaluru</h1><p>Based in Coimbatore, we provide STP manufacturing and installation, plant operation and training, AMC, RO, water softener, ETP and industrial water treatment services across Tamil Nadu, Kerala and Bengaluru.</p></div></div>\n'+JUMP+'<section style="padding-top:20px"><div class="wrap">\n'
li=lambda a:"".join(f"<li>{x}</li>" for x in a)
for s in S:
    sv_=f'<p>{s["svc"]}</p>' if isinstance(s["svc"],str) else f'<ul>{li(s["svc"])}</ul>'
    nt=f'<p>{s["note"]}</p>' if s.get("note") else ''
    islist=isinstance(s["svc"],list)
    rows=[("Best for",", ".join(s["apps"][:3])),("Includes" if islist else "Support"," &middot; ".join(s["svc"]) if islist else s["svc"]),("For a quote"," &middot; ".join(s["info"][:3]))]
    gl="".join(f"<dt>{k}</dt><dd>{v}</dd>" for k,v in rows)
    wa="https://wa.me/"+WA+"?text="+quote("Hello JP Water Treatment Solutions, I need a quote for "+s["nm"]+".")
    h+=f'''<article class="svc" id="{s["id"]}">{pic(s["k"],s["alt"])}<div><h2>{s["h"]}</h2><p>{s["intro"]}</p>
<div class="glance"><b>At a glance</b><dl>{gl}</dl></div>
<div class="btns"><a class="btn" href="/contact-us/?service={s["q"]}#quote" data-track="get_quote_click" aria-label="Get a quote for {s["nm"]}">Get a Quote</a><a class="btn line" href="{wa}" target="_blank" rel="noopener" data-track="whatsapp_click">WhatsApp Us</a></div>
<details class="fd"><summary>Full scope and quote checklist</summary><h3>{s.get("svch","Installation and maintenance")}</h3>{sv_}{nt}<h3>What to share when requesting a quote</h3><ul>{li(s["info"])}</ul></details></div>
<div class="dual"><div><h3>Problems and requirements it addresses</h3><ul>{li(s["prob"])}</ul></div><div><h3>Suitable applications</h3><ul>{li(s["apps"])}</ul></div></div></article>\n'''
h+='''</div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">How to get a quote</span><h2>Simple steps to get started</h2><div class="steps">
<div class="step"><span class="n" data-n="01" aria-hidden="true"></span><h3>Share your requirement</h3><p>Use the quote form, call us or message us on WhatsApp with your site, water source or wastewater, approximate volume and location.</p></div>
<div class="step"><span class="n" data-n="02" aria-hidden="true"></span><h3>We review the details</h3><p>We look at what you have shared and understand what your site needs.</p></div>
<div class="step"><span class="n" data-n="03" aria-hidden="true"></span><h3>We get back to you</h3><p>We contact you with the next steps for your project.</p></div></div></div></section>
<section><div class="wrap"><span class="eyebrow">Service coverage</span><h2>Where we provide our services</h2><p class="lead">Our office is in Kovaipudur, Coimbatore. We provide water treatment services in Coimbatore and across Tamil Nadu, Kerala and Bengaluru, Karnataka. Share your site location and we will discuss your requirement.</p></div></section>
'''+band("Not sure which solution you need?","Describe your requirement and we will suggest a suitable approach. Learn more <a href=\"/about-us/\" style=\"color:#b6f09c\">about our company</a>.")+FOOT
w("services",h)
# ABOUT
t="About JP Water Treatment Solutions | Coimbatore, Tamil Nadu";d="Established in 2018 in Coimbatore, JP Water Treatment Solutions has completed more than 100 projects across Tamil Nadu, Kerala and Bengaluru."
PAGES["/about-us/"]=(t,d,"About JP Water Treatment Solutions","company profile, since 2018, 100+ projects, coverage")
AFAQ=[("When was JP Water Treatment Solutions established?","We were established in 2018 and have completed more than 100 projects."),
("Where are you based?","Our office is at CBM College Road, Bharathi Nagar, Kovaipudur, Coimbatore, Tamil Nadu 641042."),
("Which areas do you serve?","We are based in Coimbatore and provide services across Tamil Nadu, Kerala and Bengaluru, Karnataka."),
("What can you do for my project?","We cover plant manufacturing, installation, operation, staff training and maintenance for STP, RO, ETP, water softener and industrial water treatment systems."),
("How do I start an enquiry?","Use the quote form on our contact page, call us or message us on WhatsApp with your site details and requirement.")]
h=head(t,d,"/about-us/",ld(LB)+crumb("About Us","/about-us/")+ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in AFAQ]}))+top("/about-us/")
A=lambda i:next(v for v in S if v["id"]==i)
lk=lambda ids:"".join(f'<li><a href="/services/#{i}">{A(i)["anc"]}</a></li>' for i in ids)
h+=f'''<div class="pagehead ph-about"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / About Us</nav><h1>About JP Water Treatment Solutions</h1><p>A water and wastewater treatment company based in Coimbatore, Tamil Nadu, serving Tamil Nadu, Kerala and Bengaluru.</p></div></div>
<section class="abt"><div class="wrap two" style="align-items:center"><div><span class="eyebrow">About us</span><h2>JP Water Treatment Solutions</h2><span class="pill">Since 2018</span>
<p>JP Water Treatment Solutions was established in 2018 and is based at CBM College Road, Bharathi Nagar, Kovaipudur, Coimbatore. We have completed more than 100 projects.</p>
<p>Our capabilities cover plant manufacturing, installation, operation, staff training and maintenance. We provide water treatment services in Coimbatore and across Tamil Nadu, Kerala and Bengaluru, Karnataka.</p>
<div class="mini"><div><b>100+</b><span>Projects completed</span></div><div><b>2018</b><span>Established</span></div><div><b>3</b><span>Regions served</span></div></div></div>
<div class="circ">{pic("ro","RO plant with membrane pressure vessels on a steel rack and white pipework",sizes="(max-width:820px) 80vw, 420px")}</div></div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">What we do</span><h2>From the plant to long-term care</h2><p class="lead">Our service capabilities, with links to the full details.</p><div class="cards">
<div class="card"><h3>Wastewater treatment</h3><ul class="checks">{lk(["stp","stp-operation","etp"])}</ul></div>
<div class="card"><h3>Water treatment</h3><ul class="checks">{lk(["ro-plant","water-softener","industrial-water-treatment"])}</ul></div>
<div class="card"><h3>Maintenance</h3><ul class="checks">{lk(["amc"])}<li>Visits monthly or every 15 days, as agreed</li><li>Detailed inspection reports</li></ul></div></div></div></section>
<section id="team"><div class="wrap"><span class="eyebrow">Our team</span><h2>People you will speak to</h2><p class="lead">Call us directly to discuss your requirement.</p><div class="cards team">{TEAMCARDS}</div></div></section>
<section class="ach" id="achievements"><div class="wrap"><span class="eyebrow light">Our achievements</span><h2>Delivering water treatment since 2018</h2>
<div class="statgrid"><div class="stat"><b data-count="100" data-suffix="+">100+</b><span>Projects completed</span></div><div class="stat"><b data-since="2018" data-suffix="+">8+</b><span>Years in water treatment</span></div><div class="stat"><b data-count="7">7</b><span>Service areas</span></div><div class="stat"><b data-count="3">3</b><span>Regions served</span></div></div></div></section>
<section class="alt"><div class="wrap"><span class="eyebrow">FAQs</span><h2>Common questions about us</h2><div class="faq"><div><div class="card"><h3>Still have a question?</h3><p>Call us, message us on WhatsApp or send the quote form.</p><div class="btns" style="margin-top:12px"><a class="btn" href="/contact-us/#quote" data-track="get_quote_click">Get a Quote</a></div></div></div>
<div>{"".join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(AFAQ))}</div></div></div></section>
<section><div class="wrap"><div class="card loc">{ico("pin")}<div><h3>Our location</h3><address>{ADDR}</address><p style="margin:.8em 0 0"><a class="more" href="{MAPS}" target="_blank" rel="noopener">View on Google Maps</a> &middot; <a class="more" href="/contact-us/">Contact us</a></p></div></div></div></section>
'''+band("Talk to our team","See all <a href=\"/services/\" style=\"color:#b6f09c\">water treatment services</a> or send us your requirement.")+FOOT
w("about-us",h)
# CONTACT
t="Contact JP Water Treatment Solutions | Coimbatore, Tamil Nadu";d="Contact JP Water Treatment Solutions in Kovaipudur, Coimbatore. Call, WhatsApp or request a quote for water treatment across Tamil Nadu, Kerala and Bengaluru."
PAGES["/contact-us/"]=(t,d,"Contact JP Water Treatment Solutions","contact / get a quote")
opts="".join(f'<option data-key="{s["q"]}">{s["nm"]}</option>' for s in S)
h=head(t,d,"/contact-us/",ld(LB)+crumb("Contact Us","/contact-us/"))+top("/contact-us/")
h+=f'''<div class="pagehead ph-contact"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Contact Us</nav><h1>Contact JP Water Treatment Solutions</h1><p>Call, message us on WhatsApp or send a quote request. We serve customers across Tamil Nadu, Kerala and Bengaluru from our base in Coimbatore.</p></div></div>
<section style="padding-bottom:30px"><div class="wrap"><div class="infogrid">
<div class="card info">{ico("pin")}<div><h2>Our office</h2><address>{NAME}<br>CBM College Road, Bharathi Nagar,<br>Kovaipudur, Coimbatore,<br>Tamil Nadu 641042</address></div></div>
<div class="card info">{ico("tel")}<div><h2>Call or WhatsApp</h2>{TEAMLINES}<p><a href="https://wa.me/{WA}" target="_blank" rel="noopener" data-track="whatsapp_click">Chat on WhatsApp</a></p></div></div>
<div class="card info">{ico("mail")}<div><h2>Email and social</h2><p><a href="mailto:{EMAIL}" data-track="email_click">{EMAIL}</a></p><p><a href="{IG}" target="_blank" rel="noopener" data-track="social_click">Instagram</a> &middot; <a href="{FB}" target="_blank" rel="noopener" data-track="social_click">Facebook</a></p></div></div>
<div class="card info">{ico("globe")}<div><h2>Service coverage</h2><p>Based in Coimbatore. Serving Tamil Nadu, Kerala and Bengaluru, Karnataka.</p></div></div>
</div></div></section>
<!-- ADD: verified business hours once confirmed -->
<section style="padding-top:30px"><div class="wrap two"><div class="formcard" id="quote"><h2>Get a Quote</h2><p class="fsub">Tell us what you need and we will get back to you.</p><form id="quote-form" novalidate>
<div class="row2"><label for="f-name">Name<input id="f-name" name="name" required aria-required="true" autocomplete="name"></label>
<label for="f-phone">Phone<input id="f-phone" name="phone" type="tel" required aria-required="true" autocomplete="tel"></label></div>
<label for="f-email">Email (optional)<input id="f-email" name="email" type="email" autocomplete="email"></label>
<div class="row2"><label for="f-service">Service<select id="f-service" name="service">{opts}<option data-key="other">Other / not sure</option></select></label>
<label for="f-loc">Your location<select id="f-loc" name="location" required aria-required="true"><option value="">Select location</option><option>Tamil Nadu</option><option>Kerala</option><option>Bengaluru, Karnataka</option><option>Other</option></select></label></div>
<label for="f-msg">Your requirement<textarea id="f-msg" name="message" rows="4" placeholder="Site type, daily water volume, location, current issue"></textarea></label>
<input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="cap"><label for="f-cap">Quick check: what is <span id="cap-q">4 + 19</span>?<input id="f-cap" name="captcha" inputmode="numeric" autocomplete="off" required aria-required="true"></label><button type="button" id="cap-new" aria-label="Show a different question">&#8635;</button></div>
<button class="btn green" type="submit">Send Enquiry</button><div id="msg" role="status" aria-live="polite"></div>
<p class="fnote">Your details are used only to respond to your enquiry. <a href="/privacy-policy/">Privacy Policy</a></p></form>
<noscript><p>Please call <a href="tel:{PHONE_T}">{PHONE_D}</a> to send an enquiry.</p></noscript></div>
<div class="mapcard"><div class="mapbox" data-src="{EMBED}" data-title="Map showing JP Water Treatment Solutions in Kovaipudur, Coimbatore"><div class="mapfacade"><svg viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.500"/></svg><p>Kovaipudur, Coimbatore. The map loads from Google when you click.</p><button type="button" class="btn map-load">Load map</button></div></div>
<div class="btns"><a class="btn" href="{GBP}" target="_blank" rel="noopener" data-track="gbp_click">Find us on Google</a><a class="btn line" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps</a></div>
<p style="margin-top:20px;color:var(--mute)">Not sure what to ask for? See our <a href="/services/">water treatment services</a> or read <a href="/about-us/">about us</a>.</p></div></div></section>
'''+FOOT
w("contact-us",h)
# PRIVACY + 404
t="Privacy Policy | JP Water Treatment Solutions";d="How JP Water Treatment Solutions handles the details you send through this website."
h=head(t,d,"/privacy-policy/",crumb("Privacy Policy","/privacy-policy/"))+top("")
h+=f'''<div class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Privacy Policy</nav><h1>Privacy Policy</h1><p>Last updated: 1 November 2026</p></div></div>
<!-- TEMPLATE: review this text (and get legal advice if needed) before publishing -->
<section><div class="wrap" style="max-width:800px"><h2>Details we collect</h2><p>When you send an enquiry through this website we receive the name, phone number, optional email address and message that you enter. If you contact us by phone or WhatsApp, those services handle your details under their own policies.</p>
<h2>How we use them</h2><p>We use your details to respond to your enquiry and prepare a quote. We do not sell them.</p>
<h2>Analytics and cookies</h2><p>If analytics is switched on, we ask for your consent first. Only after you accept do we load Google Analytics or Google Tag Manager to measure visits and clicks on call, WhatsApp and quote buttons. These tools may use cookies or similar identifiers. Your choice is saved in your browser and you can change it at any time with Cookie settings in the footer.</p>
<h2>Campaign information</h2><p>If you arrive from an advert or a link with campaign tags (such as utm or gclid), we keep those tags in your browser for the visit and send them with your enquiry so we know which advert or page brought you. They are not used to identify you.</p>
<h2>Third-party services</h2><p>This website uses Google Fonts and an embedded Google Map that loads only when you click Load map, and may use a form-processing service to deliver enquiries to us. These providers may receive technical information such as your IP address.</p>
<h2>Your choices</h2><p>To ask us to correct or delete the details you sent, contact us using the details below.</p>
<h2>Contact</h2><address>{NAME}<br>{ADDR}<br><a href="tel:{PHONE_T}">{PHONE_D}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></address>
<p><a href="/contact-us/">Contact us</a> &middot; <a href="/">Back to home</a></p></div></section>
'''+FOOT
w("privacy-policy",h)
t="Page not found | JP Water Treatment Solutions";d="The page you are looking for could not be found."
h=head(t,d,"/404.html",robots="noindex, follow").replace(f'<link rel="canonical" href="{BASE}/404.html">\n','')+top("")
h+='''<section><div class="wrap" style="text-align:center;max-width:640px"><h1>Page not found</h1><p class="lead" style="margin:0 auto 1.2em">That page does not exist or has moved. Try one of these pages.</p>
<div class="btns" style="justify-content:center"><a class="btn" href="/">Home</a><a class="btn line" href="/services/">Services</a><a class="btn line" href="/about-us/">About Us</a><a class="btn line" href="/contact-us/">Contact Us</a></div></div></section>
'''+FOOT
open("out/404.html","w").write(h)
# sitemap, robots
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f'  <url><loc>{BASE}{p}</loc><lastmod>2026-10-27</lastmod></url>\n' for p in PAGES)+'</urlset>\n'
open("out/sitemap.xml","w").write(sm)
open("out/robots.txt","w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
for p,(t,d,h1,k) in PAGES.items():print(p,len(t),len(d),"|",t,"|",h1)
