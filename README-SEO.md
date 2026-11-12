# JP Water Treatment Solutions: SEO build notes

## Structure (static HTML, root-relative URLs)
/ (index.html) · /services/ · /about-us/ · /contact-us/ · /assets/style.css · /assets/site.js · /public/images/ · sitemap.xml · robots.txt
Serve from the domain root. Test locally with: `python3 -m http.server 8000` (open http://localhost:8000/). Opening files by double-click will not load CSS/images because paths start with "/".

## Before launch (required)
1. Replace the placeholder domain: `./set-domain.sh https://www.yourrealdomain.com` (canonicals, Open Graph, JSON-LD, sitemap.xml, robots.txt).
2. Set IDs in `assets/site.js` (top of file): GA4_ID, GTM_ID, FORM_ENDPOINT (or BUSINESS_EMAIL). Leave blank to disable.
3. Search Console: add the HTML-tag meta where the comment sits in each page head (or verify by DNS), then submit https://yourdomain/sitemap.xml.
4. Confirm the phone number +91 99948 85701 (used in pages and LocalBusiness data).
5. Redirect http→https and www/non-www to one version; configure a real 404 page on the host.

## Tracking events (GA4 / GTM dataLayer)
get_quote_click, call_click, whatsapp_click (on click), generate_lead (only after the form endpoint returns success; never on button click, WhatsApp fallback or mailto fallback).

## Still needed from the business
exact Google Maps place URL for the schema (the current Google share link is used) · verified business hours (optional) · confirmation that installation is offered for each service · confirmed service areas · real project photos for the Projects placeholders · higher-resolution service images · real client testimonials only if permitted.


Extra files: 404.html (noindex), privacy-policy/ (template, not in sitemap), .htaccess (Apache) and _headers (Netlify/Cloudflare), set-domain.sh, SETUP-GUIDE.md (step-by-step with exact URLs), assets/logo.svg, favicons, public/images/og-share.jpg.

## Content update (Tamil Nadu, Kerala & Bengaluru)
Home H1 and supporting text updated; Coimbatore kept as the base. Services page now has 7 sections (new: STP Plant Operation, Manpower and Training; AMC, STP and RO sections rewritten with the actual scope). About Us includes established 2018, 100+ projects and coverage. Coverage wording never implies offices outside Coimbatore. Structured data uses areaServed = Tamil Nadu, Kerala, Bengaluru and foundingDate 2018; the business address stays Coimbatore only.

## Polish update
- Projects section is commented out in index.html (search for "PROJECTS SECTION"); remove the comment markers and add real photos to show it.
- Trust strip under the hero, sticky service jump bar on /services/, Location dropdown in the quote form (sent with the enquiry and with the generate_lead event), mobile bottom bar (Call | WhatsApp | Get a Quote), Call/WhatsApp cards on /contact-us/, footer logo.
- Accent colour is now the logo green (#277d19 for text and buttons, white text passes AA contrast). Font weights reduced to Inter 400/600 and Plus Jakarta Sans 700/800.

## Motion update
Home page now follows a richer section flow: hero (slow zoom, floating water drop, wave), About with checklist, tabbed Solutions (Water / Wastewater / Operation & Maintenance), End-to-end support steps, animated achievement counters, why-choose-us, coverage, services ticker, FAQ with side blocks, CTA. Header has a Services dropdown and a Get a Quote button. Scroll-reveal, hover and counter animations live in assets/style.css and assets/site.js and switch off for visitors who prefer reduced motion.
Three sections are built but switched off until real content exists: Clients (logo marquee), Customer feedback (Google reviews slider), Projects. Each sits in an HTML comment in index.html (look for OPT-CLIENTS, OPT-TESTI (Customer feedback), OPT-PROJECTS); remove the comment markers and replace the sample content to show them.

## Contact details on the site
Email JpwaterSolution04@gmail.com, Instagram https://www.instagram.com/jp_water_treatment_solutions and Facebook https://www.facebook.com/share/1F3FQxB7rf/ appear on the Contact page, footer and structured data (sameAs). Use the same email in Formspree (SETUP-GUIDE step 3) so enquiries arrive there. Leave BUSINESS_EMAIL in assets/site.js blank, otherwise the form opens the visitor's mail app instead of sending.

## Services/About/Contact update
Services page: each service has an At a glance box, buttons (quote + service-specific WhatsApp message) and a Full details accordion; sections alternate image left/right; a How to get a quote steps block was added. About page has a company FAQ (also FAQPage structured data). The quote form has a simple maths check (deters basic bots only; turn on Formspree spam filtering too). Back-to-top button added.

## Project gallery
Home page now has a live Our projects gallery with three real photos (sewage treatment plant, RO plant, water softener) in public/images/projects/ (800px thumbnails and 1536px lightbox versions, JPG + WebP). To add a photo, resize it to 1536x1024, save the two sizes, and copy one figure with class gitem in index.html.

## Real photos placement
Real photos are used for: Home hero (rooftop vessels), service cards and Services page sections for STP, RO, Water Softener and AMC, Home About image (STP plant room), About page circle (RO plant) and the Home gallery (5 photos). AI illustrations remain only for STP Operation, ETP and Industrial Water Treatment until real photos are available. Responsive sizes: 800px and 1536px (JPG + WebP) in public/images/projects/.

## Four-change update
1) Home About image: 2018 Established card is a centred navy bar under the image (no random offsets). 2) CTA buttons are pill-shaped, uppercase and a consistent height, in the original colours (blue primary, green WhatsApp/Send Enquiry, white-outline secondary on dark areas, blue-outline on light areas) (applies to Get a Quote, WhatsApp, Call Now, Contact, Maps/Google, enquiry and service buttons; actions unchanged). 3) ETP card/section uses the technician-at-vessel photo. 4) AMC uses its own illustration (AI-generated, labelled as an illustration in the alt text, not a real project photo); STP Operation uses the rooftop vessels photo. Floating Call, WhatsApp and Instagram icons are circular with coloured glows (Instagram: https://www.instagram.com/jp_water_treatment_solutions). On phones the bottom bar keeps Call/WhatsApp/Get a Quote and the Instagram icon floats above it.

## Polish pass
Logos are WebP; unused CSS rules removed (checked with before/after screenshots); the achievements band uses a real plant photo. Reviews slider and services ticker have Pause buttons; mobile menu has a Services accordion; form shows the first error and focuses the field, and a fuller thank-you message after a successful send. Home order is now: hero, about, solutions, projects, customer feedback, support steps, achievements, why us, coverage, ticker, FAQ, CTA. CSS and JS links carry a version (?v=20261030): when you edit assets/style.css or assets/site.js, change that number in every HTML file so visitors get the new file. Server caching for CSS/JS is now 1 month.

## Alignment and mobile pass
About image (Home): grid container; decorative outline sits behind the image (offset up-left); the 2018 Established card has exactly the image width with a fixed overlap (30px desktop, 22px mobile). Service sections on /services/: image always left, content right, image vertically centred against the whole content column (5:4 on desktop, 16:10 stacked on tablet and phone). Phones: floating icons are hidden and Call / WhatsApp / Get a Quote / Instagram live in the bottom bar; back-to-top is hidden on phones so nothing covers text or form fields. Tap targets enlarged (slider controls, FAQ rows, breadcrumbs, footer links). Tested at 360, 390, 768, 1024 and 1440 px on every page: no horizontal scrolling.

## Batch 1 (Home trim, call-back forms, maths switch)
Home now has: hero (with a Request a call back card on desktop), about, solutions, projects, customer feedback, support steps plus where systems are used, counters plus coverage, FAQ, CTA. The why-choose-us, coverage and services-ticker sections were merged or removed, and the duplicate enquiry steps were removed from About. A name+phone Call me back strip is in every page footer (the hero card is hidden on phones). Both call-back forms post to FORM_ENDPOINT with service 'Call back request' and fire generate_lead with lead_type=callback only after a successful send. JP_CONFIG.MATH_CHECK (assets/site.js) switches the quote-form maths question on or off. Legacy duplicate reveal and slider code was removed from site.js.

## Batches 2 and 3
Lead source: utm_*, gclid, fbclid, gbraid, wbraid and the landing page are kept in sessionStorage for the visit and sent with the quote form and call-back forms (lead_source plus the raw fields), and added to WhatsApp/email fallback messages and the generate_lead event. Cookie banner: GA4/GTM load only after Accept (no banner when no IDs are set; Cookie settings link in the footer reopens it). Page-specific share images: og-share (home), og-services, og-about, og-contact. Contact page map loads only after Load map is clicked. Services: Problems and Applications lists are now visible under each service (full width row), the accordion keeps the full scope and quote checklist. Motion: one-time hero zoom only; wave, bubbles and parallax are static. Fonts: size-matched fallback faces added. Headers: X-Frame-Options and Permissions-Policy added (HSTS line ready to enable). Carousel has region/slide semantics. A source/ folder (build.py and notes) ships next to the site folder in the zip.

## Team details
Managing Director Salaman Raj S (+91 99948 85701) and Manager Alexander S (+91 98430 10518), taken from the business card, appear in: About page (Our team cards with Call buttons), Contact page (Call or WhatsApp card), footer (Get in Touch) and LocalBusiness structured data (employee). The Managing Director's number is also the site's main phone and WhatsApp number. Email is shown in lower case as printed on the card. To change a name, role or number edit TEAM at the top of source/build.py (and the footer line).

## Hero card removed, About frame
The Request a call back card was removed from the Home hero (the Call me back strip stays in every page footer). The Home About image now sits inside its blue outline frame together with the 2018 Established card: equal padding on all sides, card the same width as the image, fixed overlap (28px desktop, 22px phone).

## Service image alignment
On /services/ the image is now aligned to the top of each section (level with the heading) and stays in view (sticky, 140px from the top) while the longer text on the right scrolls. On tablets and phones it is not sticky and sits above the heading. The same rule applies to all seven service sections.

## Photo banners
Services, About and Contact page banners now sit on real project photos (RO plant, STP plant room, pressure vessel) with a navy overlay and a dimmed centre so the headline stays readable. WebP is used where supported with a JPG fallback, and 800px versions are used on phones. Privacy and 404 keep the plain gradient banner. Breadcrumb alignment was fixed and the services jump bar no longer shows a scrollbar.

## UI/UX review pass
Hero: badge 'Based in Coimbatore, Tamil Nadu', supporting text now ends 'Serving customers across Tamil Nadu, Kerala, and Bengaluru.', Get a Quote primary with Call Now and WhatsApp Us as outline secondaries (same in CTA bands; service sections say WhatsApp Us), balanced hero height. Services: category pills highlight the section being read (aria-current), each service image is centred against the whole right column at a fixed 4:3 frame (16:10 stacked on phones), the At a glance card is never clipped, the key lists sit in a full-width row below. Laptop widths (821-1270px) keep an 88px right gutter so the floating icons never cover text. Forms: when no endpoint is set the message says plainly that nothing has been sent yet, and a blocked WhatsApp window shows a tap-to-open link instead of claiming success. About page circle slightly smaller.
