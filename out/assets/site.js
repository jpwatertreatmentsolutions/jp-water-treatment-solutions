/* ===== CONFIGURE BEFORE GOING LIVE =====
   GA4_ID  : Google Analytics 4 Measurement ID, e.g. "G-XXXXXXXXXX" (leave "" to disable)
   GTM_ID  : Google Tag Manager container ID, e.g. "GTM-XXXXXXX" (leave "" to disable)
   If GTM_ID is set, GA4 should be configured inside GTM (events are pushed to dataLayer).
   FORM_ENDPOINT : URL that receives enquiries (e.g. Formspree) and emails them to the business.
   BUSINESS_EMAIL: optional mailto fallback if no endpoint is set.
   Analytics (GA4/GTM) loads only after the visitor clicks Accept in the cookie banner; with no IDs set there is no banner.
   MATH_CHECK    : true shows the quick maths question on the quote form; set false once the form service's spam filter is on. */
var JP_CONFIG={GA4_ID:"",GTM_ID:"",FORM_ENDPOINT:"",BUSINESS_EMAIL:"",WHATSAPP:"919994885701",MATH_CHECK:true};
(function(){
var C=JP_CONFIG;window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
function load(src){var s=document.createElement("script");s.async=true;s.src=src;document.head.appendChild(s)}
var started=false;
function startAnalytics(){if(started)return;started=true;
 if(C.GTM_ID){dataLayer.push({"gtm.start":Date.now(),event:"gtm.js"});load("https://www.googletagmanager.com/gtm.js?id="+encodeURIComponent(C.GTM_ID))}
 else if(C.GA4_ID){load("https://www.googletagmanager.com/gtag/js?id="+encodeURIComponent(C.GA4_ID));gtag("js",new Date());gtag("config",C.GA4_ID)}}
function track(name,p){p=p||{};if(C.GTM_ID){var o={event:name};for(var k in p)o[k]=p[k];dataLayer.push(o)}else if(C.GA4_ID){gtag("event",name,p)}}
window.jpTrack=track;
/* campaign attribution kept for the visit (sessionStorage) and sent with enquiries */
var AK=["utm_source","utm_medium","utm_campaign","utm_term","utm_content","gclid","fbclid","gbraid","wbraid"];
function getAttr(){var a={};try{a=JSON.parse(sessionStorage.getItem("jp_attr")||"{}")}catch(e){}
 var q=new URLSearchParams(location.search),fresh={},has=false;AK.forEach(function(k){var v=q.get(k);if(v){fresh[k]=v.slice(0,120);has=true}});
 if(has){a=fresh;a.landing_page=location.pathname}
 else if(!a.landing_page){a.landing_page=location.pathname;try{var h=new URL(document.referrer).hostname;if(h&&h!==location.hostname)a.referrer=h}catch(e){}}
 try{sessionStorage.setItem("jp_attr",JSON.stringify(a))}catch(e){}return a}
var ATTR=getAttr();
function srcLabel(a){if(a.utm_source)return a.utm_source+(a.utm_medium?" / "+a.utm_medium:"")+(a.utm_campaign?" / "+a.utm_campaign:"");if(a.gclid||a.gbraid||a.wbraid)return "Google Ads";if(a.fbclid)return "Meta (Facebook/Instagram)";if(a.referrer)return "Referral: "+a.referrer;return "Direct"}
window.jpAttr=function(){return ATTR};window.jpSrc=function(){return srcLabel(ATTR)};
/* cookie consent: analytics only after Accept */
var hasA=!!(C.GTM_ID||C.GA4_ID),cb=document.getElementById("consent"),cs=document.getElementById("cookie-settings");
function getC(){try{return localStorage.getItem("jp_consent")}catch(e){return null}}
function setC(v){try{localStorage.setItem("jp_consent",v)}catch(e){}}
if(hasA){if(cs)cs.hidden=false;var cur=getC();if(cur==="granted")startAnalytics();else if(cur!=="denied"&&cb)cb.hidden=false;
 if(cb){document.getElementById("consent-yes").addEventListener("click",function(){setC("granted");cb.hidden=true;startAnalytics()});
  document.getElementById("consent-no").addEventListener("click",function(){var was=getC()==="granted";setC("denied");cb.hidden=true;if(was)location.reload()});
  if(cs)cs.addEventListener("click",function(){cb.hidden=false;document.getElementById("consent-yes").focus()})}}
document.addEventListener("click",function(e){var t=e.target.closest("[data-track]");if(t)track(t.getAttribute("data-track"),{link_text:(t.textContent||"").trim().slice(0,60)})});
var m=document.getElementById("menu"),l=document.getElementById("links");
if(m)m.addEventListener("click",function(){var o=l.classList.toggle("open");m.setAttribute("aria-expanded",o)});
var f=document.getElementById("quote-form");if(!f)return;
var cap={a:0,b:0};function newCap(){cap.a=2+Math.floor(Math.random()*18);cap.b=2+Math.floor(Math.random()*18);var q=document.getElementById("cap-q");if(q)q.textContent=cap.a+" + "+cap.b;if(f.elements.captcha)f.elements.captcha.value=""}
newCap();var cn=document.getElementById("cap-new");if(cn)cn.addEventListener("click",newCap);
if(C.MATH_CHECK===false){var cw=document.querySelector(".cap");if(cw)cw.style.display="none";if(f.elements.captcha){f.elements.captcha.required=false;f.elements.captcha.removeAttribute("aria-required")}}
function bad(el){if(el){el.setAttribute("aria-invalid","true");el.focus()}}
f.addEventListener("input",function(e){if(e.target.removeAttribute)e.target.removeAttribute("aria-invalid")});
var sel=f.elements.service,q=new URLSearchParams(location.search).get("service");
if(q&&sel)for(var i=0;i<sel.options.length;i++)if(sel.options[i].getAttribute("data-key")===q)sel.selectedIndex=i;
f.addEventListener("submit",function(e){
 e.preventDefault();var msg=document.getElementById("msg"),d={};new FormData(f).forEach(function(v,k){d[k]=v});
 if(d.website)return;

 if(!d.name.trim()||d.phone.replace(/\D/g,"").length<10){msg.style.color="#b3261e";msg.textContent="Please enter your name and a valid phone number.";bad(!d.name.trim()?f.elements.name:f.elements.phone);return}
 if(!d.location){msg.style.color="#b3261e";msg.textContent="Please select your location.";bad(f.elements.location);return}
 if(C.MATH_CHECK!==false&&f.elements.captcha&&parseInt(d.captcha,10)!==cap.a+cap.b){msg.style.color="#b3261e";msg.textContent="Please answer the quick maths question correctly.";newCap();bad(f.elements.captcha);return}
 delete d.captcha;
 var at=ATTR;for(var ak in at)d[ak]=at[ak];d.lead_source=srcLabel(at);
 var text="New enquiry - JP Water Treatment Solutions\nName: "+d.name+"\nPhone: "+d.phone+"\nEmail: "+(d.email||"-")+"\nLocation: "+d.location+"\nService: "+d.service+"\nDetails: "+(d.message||"-")+"\nSource: "+d.lead_source+"\nLanding page: "+(at.landing_page||"-");
 if(C.FORM_ENDPOINT){
  msg.style.color="#1c2b3a";msg.textContent="Sending...";
  fetch(C.FORM_ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(d)})
  .then(function(r){if(!r.ok)throw 0;track("generate_lead",{service:d.service,location:d.location,lead_source:d.lead_source});msg.style.color="#126b3f";msg.innerHTML='Thank you! We have received your enquiry and will contact you soon. For a faster reply, <a href="tel:+'+C.WHATSAPP+'">call us</a> or <a href="https://wa.me/'+C.WHATSAPP+'" target="_blank" rel="noopener">message us on WhatsApp</a>.';msg.setAttribute("tabindex","-1");msg.focus();f.reset();newCap()})
  .catch(function(){msg.style.color="#b3261e";msg.textContent="Sorry, your enquiry could not be sent. Please call or WhatsApp us."});
 }else if(C.BUSINESS_EMAIL){location.href="mailto:"+C.BUSINESS_EMAIL+"?subject="+encodeURIComponent("Quote request: "+d.service)+"&body="+encodeURIComponent(text);msg.style.color="#1c2b3a";msg.textContent="Your email app should open with your enquiry. Please press send there. Nothing has been sent yet."}
 else{var wu="https://wa.me/"+C.WHATSAPP+"?text="+encodeURIComponent(text),w=window.open(wu,"_blank");msg.style.color="#1c2b3a";if(w){try{w.opener=null}catch(x){}msg.textContent="WhatsApp opened with your enquiry. Please press send there. Nothing has been sent yet."}else{msg.innerHTML='Your browser blocked the WhatsApp window. <a href="'+wu+'" target="_blank" rel="noopener">Tap here to send your enquiry on WhatsApp</a>. Nothing has been sent yet.'}}
});
})();

/* Motion and interactive sections: header shadow, scroll reveal, counters, tabs, testimonial slider */
(function(){
var d=document,rm=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
var hd=d.querySelector("header.site");function sc(){if(hd)hd.classList.toggle("scrolled",window.scrollY>10)}
window.addEventListener("scroll",sc,{passive:true});sc();
function count(el){var s=el.getAttribute("data-since"),t=s?new Date().getFullYear()-parseInt(s,10):parseInt(el.getAttribute("data-count"),10),suf=el.getAttribute("data-suffix")||"";
 if(rm){el.textContent=t+suf;return}
 var st=null;el.textContent="0"+suf;
 function step(ts){if(!st)st=ts;var p=Math.min((ts-st)/1600,1),e=1-Math.pow(1-p,3);el.textContent=Math.round(t*e)+suf;if(p<1)requestAnimationFrame(step)}
 requestAnimationFrame(step)}
if("IntersectionObserver" in window){
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;io.unobserve(el);
  if(el.hasAttribute("data-count")||el.hasAttribute("data-since")){count(el);return}
  el.classList.add("in");setTimeout(function(){el.classList.remove("rv","in");el.style.transitionDelay=""},1300)})},{threshold:.12,rootMargin:"0px 0px -40px 0px"});
 if(!rm)d.querySelectorAll("main section h2,main section .eyebrow,main .lead,main .card,main .svc,main .chips span,main details,main .step,main .about-img,main .checks li,main .gitem,.cta .wrap>*").forEach(function(el){
  el.classList.add("rv");var k=Array.prototype.indexOf.call(el.parentNode.children,el);el.style.transitionDelay=Math.min(k,4)*60+"ms";io.observe(el)});
 d.querySelectorAll("[data-count],[data-since]").forEach(function(el){io.observe(el)});
}
var tt=d.getElementById("totop");if(tt){window.addEventListener("scroll",function(){tt.classList.toggle("show",window.scrollY>600)},{passive:true});tt.addEventListener("click",function(){window.scrollTo({top:0,behavior:rm?"auto":"smooth"})})}
var lb=d.getElementById("lb");if(lb&&lb.showModal){d.querySelectorAll("a.gal").forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();var im=a.querySelector("img"),big=d.getElementById("lb-img");big.src=a.href;big.alt=im.alt;d.getElementById("lb-cap").textContent=a.getAttribute("data-cap")||"";lb.showModal()})});lb.addEventListener("click",function(e){if(e.target===lb||e.target.classList.contains("lb-x"))lb.close()})}
d.querySelectorAll(".sub-toggle").forEach(function(b){b.addEventListener("click",function(){var li=b.parentNode,o=li.classList.toggle("open");b.setAttribute("aria-expanded",o);b.setAttribute("aria-label",o?"Hide services menu":"Show services menu")})});
d.querySelectorAll(".tabs").forEach(function(tb){var b=tb.querySelectorAll("button"),p=[];b.forEach(function(x){p.push(d.getElementById(x.getAttribute("aria-controls")))});
 function show(i){b.forEach(function(x,k){x.setAttribute("aria-selected",k===i);x.tabIndex=k===i?0:-1;p[k].hidden=k!==i})}
 b.forEach(function(x,i){x.addEventListener("click",function(){show(i)});x.addEventListener("keydown",function(e){if(e.key==="ArrowRight"||e.key==="ArrowLeft"){var n=(i+(e.key==="ArrowRight"?1:b.length-1))%b.length;show(n);b[n].focus()}})});show(0)});
d.querySelectorAll("[data-slider]").forEach(function(sl){var tr=sl.querySelector(".slides"),sd=sl.querySelectorAll(".slide"),dt=sl.querySelector(".dots"),pb=sl.querySelector(".pp"),paused=false,i=0,tm;
 sl.setAttribute("role","region");sl.setAttribute("aria-roledescription","carousel");sl.setAttribute("aria-label","Customer reviews");sd.forEach(function(s,k){s.setAttribute("role","group");s.setAttribute("aria-roledescription","slide");s.setAttribute("aria-label",(k+1)+" of "+sd.length)});
 sd.forEach(function(_,k){var b=d.createElement("button");b.type="button";b.setAttribute("aria-label","Go to testimonial "+(k+1));b.addEventListener("click",function(){go(k,1)});dt.appendChild(b)});
 function go(n,u){i=(n+sd.length)%sd.length;sd.forEach(function(s,k){s.setAttribute("aria-hidden",k===i?"false":"true")});tr.style.transform="translateX(-"+i*100+"%)";Array.prototype.forEach.call(dt.children,function(b,k){b.setAttribute("aria-current",k===i)});if(u)rs()}
 function rs(){clearInterval(tm);if(!rm&&!paused)tm=setInterval(function(){go(i+1)},6500)}
 sl.querySelector(".prev").addEventListener("click",function(){go(i-1,1)});sl.querySelector(".next").addEventListener("click",function(){go(i+1,1)});
 if(pb)pb.addEventListener("click",function(){paused=!paused;pb.setAttribute("aria-pressed",paused);pb.setAttribute("aria-label",paused?"Resume automatic review rotation":"Pause automatic review rotation");pb.innerHTML=paused?"&#9654;":"&#10074;&#10074;";rs()});
 sl.addEventListener("mouseenter",function(){clearInterval(tm)});sl.addEventListener("mouseleave",rs);
 var x0=null;sl.addEventListener("touchstart",function(e){x0=e.touches[0].clientX},{passive:true});sl.addEventListener("touchend",function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)go(i+(dx<0?1:-1),1);x0=null});
 go(0);rs()});
})();

/* Call-back forms (hero card and footer strip): name + phone only */
(function(){var C=window.JP_CONFIG||{};
document.querySelectorAll("form.cb-form").forEach(function(f){var msg=f.querySelector(".cb-msg");
 f.addEventListener("input",function(e){if(e.target.removeAttribute)e.target.removeAttribute("aria-invalid")});
 f.addEventListener("submit",function(e){e.preventDefault();var d={};new FormData(f).forEach(function(v,k){d[k]=v});if(d.website)return;
  function err(t,el){msg.className="cb-msg err";msg.textContent=t;if(el){el.setAttribute("aria-invalid","true");el.focus()}}
  function ok(t){msg.className="cb-msg";msg.textContent=t}
  if(!d.name.trim()){err("Please enter your name.",f.elements.name);return}
  if(d.phone.replace(/\D/g,"").length<10){err("Please enter a valid phone number.",f.elements.phone);return}
  var src=f.getAttribute("data-src")||"callback",payload={name:d.name,phone:d.phone,service:"Call back request",message:"Please call me back.",source:src};var at2=window.jpAttr?jpAttr():{};for(var ak2 in at2)payload[ak2]=at2[ak2];payload.lead_source=window.jpSrc?jpSrc():"";
  if(C.FORM_ENDPOINT){ok("Sending...");
   fetch(C.FORM_ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(payload)})
   .then(function(r){if(!r.ok)throw 0;if(window.jpTrack)jpTrack("generate_lead",{lead_type:"callback",source:src,lead_source:payload.lead_source});ok("Thank you! We will call you back soon.");f.reset()})
   .catch(function(){err("Sorry, we could not send this. Please call or WhatsApp us.")});
  }else if(C.BUSINESS_EMAIL){location.href="mailto:"+C.BUSINESS_EMAIL+"?subject="+encodeURIComponent("Call back request")+"&body="+encodeURIComponent("Please call me back.\nName: "+d.name+"\nPhone: "+d.phone+"\nSource: "+(payload.lead_source||"-"));ok("Your email app should open. Please press send there. Nothing has been sent yet.")}
  else{var wu2="https://wa.me/"+C.WHATSAPP+"?text="+encodeURIComponent("Please call me back.\nName: "+d.name+"\nPhone: "+d.phone+"\nSource: "+(payload.lead_source||"-")),w2=window.open(wu2,"_blank");if(w2){try{w2.opener=null}catch(x){}ok("WhatsApp opened with your request. Please press send there. Nothing has been sent yet.")}else{msg.className="cb-msg";msg.innerHTML='Your browser blocked the WhatsApp window. <a href="'+wu2+'" target="_blank" rel="noopener">Tap here to send your request on WhatsApp</a>. Nothing has been sent yet.'}}
 })})})();

/* Map loads from Google only after the visitor clicks Load map */
(function(){var mb=document.querySelector(".mapbox");if(!mb)return;var btn=mb.querySelector(".map-load");if(!btn)return;
btn.addEventListener("click",function(){var i=document.createElement("iframe");i.src=mb.getAttribute("data-src");i.title=mb.getAttribute("data-title")||"Map";i.setAttribute("referrerpolicy","no-referrer-when-downgrade");i.setAttribute("allowfullscreen","");mb.innerHTML="";mb.appendChild(i)})})();

/* Services category pills: highlight the section being read */
(function(){var jump=document.querySelector(".jump");if(!jump||!("IntersectionObserver" in window))return;
var links={};jump.querySelectorAll("a[href^='#']").forEach(function(a){links[a.getAttribute("href").slice(1)]=a});
function set(id){Object.keys(links).forEach(function(k){var on=k===id;links[k].classList.toggle("on",on);if(on)links[k].setAttribute("aria-current","true");else links[k].removeAttribute("aria-current")});
 var a=links[id],w=jump.querySelector(".wrap");if(a&&w&&w.scrollWidth>w.clientWidth){w.scrollTo({left:a.offsetLeft-(w.clientWidth-a.offsetWidth)/2,behavior:"smooth"})}}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)set(e.target.id)})},{rootMargin:"-35% 0px -55% 0px"});
document.querySelectorAll(".svc").forEach(function(s){io.observe(s)});
jump.addEventListener("click",function(e){var a=e.target.closest("a[href^='#']");if(a)set(a.getAttribute("href").slice(1))})})();
