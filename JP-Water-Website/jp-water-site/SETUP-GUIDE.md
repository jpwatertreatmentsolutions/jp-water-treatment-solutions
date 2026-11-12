# Setup guide (do these in order)

## 1. Put the real domain in the site
1. Buy or choose your domain (example: https://www.yourdomain.com).
2. In this folder run: `./set-domain.sh https://www.yourdomain.com` (Mac/Linux/Git Bash). Without a terminal, use any editor's Find & Replace on all .html, .xml and .txt files: replace `https://YOUR-DOMAIN.com` with your domain.

## 2. Upload (pick your host)
- cPanel / Hostinger: File Manager > public_html > upload everything in this folder (including the hidden `.htaccess`).
- Netlify: https://app.netlify.com/drop > drag this folder in. (`_headers` is used; ignore `.htaccess`.)
- Cloudflare Pages: https://dash.cloudflare.com > Workers & Pages > Create > Pages > Upload assets.
Then open https://yourdomain.com and click all four pages.

## 3. Form delivery to your email (Formspree)
1. Go to https://formspree.io > Sign up > New Form > enter the business email.
2. Copy the form URL (looks like https://formspree.io/f/xxxxxxx).
3. Open `assets/site.js`, paste it into `FORM_ENDPOINT:""`, save, re-upload.
4. Send a test enquiry. In Formspree, turn on spam protection in the form's Settings.
5. Once spam protection is on, open `assets/site.js` and change `MATH_CHECK:true` to `MATH_CHECK:false` to remove the maths question from the quote form. The Call me back strip in the footer uses the same FORM_ENDPOINT and needs no change.

## 4. Google Search Console
1. Open https://search.google.com/search-console > Add property > URL prefix > enter your site URL.
2. Choose "HTML tag", copy the meta tag, paste it where the comment says "Google Search Console" in the `<head>` of all 4 pages, re-upload, click Verify.
3. Sidebar > Sitemaps > enter `sitemap.xml` > Submit.
4. URL inspection > paste each of the 4 URLs > Request indexing.

## 5. Google Analytics 4 (GA4)
1. https://analytics.google.com > Admin > Create > Property > then Data streams > Web > enter your URL.
2. Copy the Measurement ID (G-XXXXXXXXXX) into `GA4_ID` in `assets/site.js`.
3. After a test enquiry, go to Admin > Events and mark `generate_lead`, `call_click`, `whatsapp_click` and `get_quote_click` as key events (the toggle named "Mark as key event").
(Using Tag Manager instead? Put the GTM-XXXXXXX ID in `GTM_ID` and set up GA4 inside https://tagmanager.google.com. Do not fill both IDs.)

## 6. Google Business Profile
1. https://business.google.com > open JP Water Treatment Solutions.
2. Add website, services, categories, photos, phone. Keep name, address and phone exactly the same as the website footer.
3. To get a review link: Profile > "Get more reviews" > copy the link. Send it to real customers (ask me to add a "Review us on Google" button).
4. For the map: Maps > search your business > Share > Embed a map > copy the iframe src into the Contact page.

## 7. Check before announcing
- https://search.google.com/test/rich-results (test the Home, Services and Contact URLs)
- https://pagespeed.web.dev (check mobile score)
- Test on a real phone: menu, call button, WhatsApp, form.
- Review /privacy-policy/ (it is a template, not legal advice).
