"""Builds the legal pages (privacy, terms, dpa) and 404.html from one shell, so nav, footer and
type stay identical to the rest of the site.  Run:  python3 legal-build.py   (from engine/site)."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
UPDATED = "12 October 2026"
OPERATOR = ("WOGO Amsterdam B.V., Oude-IJsselstraat 32-2, 1078 CP Amsterdam, the Netherlands. "
            "Chamber of Commerce (KvK) 92237347, VAT NL865949323B01. Contact: hello@kalmly.io.")

WM = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="wm" viewBox="0 0 660 190"><g transform="translate(6,146)">
<path style="fill:var(--wm-k,#F3F6FB)" d="M12.98828125 0.0V-146.484375H47.265625V-67.48046875L84.375 -105.46875H122.0703125L83.88671875 -66.2109375L123.73046875 0.0H86.03515625L61.23046875 -42.48046875L47.265625 -28.02734375V0.0Z"/>
<path style="fill:var(--wm-k,#F3F6FB)" d="M161.06640625 2.5390625Q151.203125 2.5390625 142.365234375 -0.78125Q133.52734375 -4.1015625 128.05859375 -11.1328125Q122.58984375 -18.1640625 122.58984375 -29.39453125Q122.58984375 -41.50390625 129.572265625 -49.365234375Q136.5546875 -57.2265625 149.298828125 -61.1328125Q162.04296875 -65.0390625 179.62109375 -65.0390625H193.29296875L191.53515625 -61.9140625V-68.1640625Q191.53515625 -77.734375 188.263671875 -82.12890625Q184.9921875 -86.5234375 177.47265625 -86.5234375Q170.1484375 -86.5234375 166.33984375 -82.6171875Q162.53125 -78.7109375 161.359375 -71.19140625L127.1796875 -76.7578125Q129.1328125 -85.64453125 135.138671875 -92.7734375Q141.14453125 -99.90234375 152.033203125 -104.1015625Q162.921875 -108.30078125 179.328125 -108.30078125Q193.78125 -108.30078125 204.083984375 -104.00390625Q214.38671875 -99.70703125 219.904296875 -89.35546875Q225.421875 -79.00390625 225.421875 -60.7421875V-29.8828125Q225.421875 -26.5625 226.349609375 -25.48828125Q227.27734375 -24.4140625 230.3046875 -24.4140625H234.6015625V0.0H219.3671875Q206.0859375 0.0 199.54296875 -6.396484375Q193.0 -12.79296875 193.0 -25.1953125V-29.1015625L199.25 -26.46484375Q198.078125 -22.16796875 195.783203125 -17.1875Q193.48828125 -12.20703125 189.2890625 -7.71484375Q185.08984375 -3.22265625 178.205078125 -0.341796875Q171.3203125 2.5390625 161.06640625 2.5390625ZM171.3203125 -19.7265625Q177.66796875 -19.7265625 182.2578125 -22.55859375Q186.84765625 -25.390625 189.38671875 -30.76171875Q191.92578125 -36.1328125 191.92578125 -43.75V-46.58203125H181.28125Q171.90625 -46.58203125 166.73046875 -44.140625Q161.5546875 -41.69921875 159.552734375 -38.18359375Q157.55078125 -34.66796875 157.55078125 -31.4453125Q157.55078125 -29.296875 158.625 -26.5625Q159.69921875 -23.828125 162.62890625 -21.77734375Q165.55859375 -19.7265625 171.3203125 -19.7265625Z"/>
<path style="fill:var(--wm-k,#F3F6FB)" d="M273.109375 0.0Q259.14453125 0.0 252.2109375 -6.34765625Q245.27734375 -12.6953125 245.27734375 -25.1953125V-146.484375H279.5546875V-29.8828125Q279.5546875 -26.5625 280.482421875 -25.48828125Q281.41015625 -24.4140625 284.4375 -24.4140625H291.6640625V0.0Z"/>
<path style="fill:var(--wm-k,#F3F6FB)" d="M301.4609375 0.0V-105.46875H334.76171875V-88.96484375Q339.7421875 -98.53515625 347.701171875 -103.3203125Q355.66015625 -108.10546875 366.3046875 -108.10546875Q377.53515625 -108.10546875 385.0546875 -102.783203125Q392.57421875 -97.4609375 396.1875 -87.109375Q402.53515625 -98.53515625 411.568359375 -103.3203125Q420.6015625 -108.10546875 430.26953125 -108.10546875Q446.578125 -108.10546875 454.9765625 -96.6796875Q463.375 -85.25390625 463.375 -63.4765625V0.0H429.1953125V-64.453125Q429.1953125 -69.23828125 428.21875 -73.388671875Q427.2421875 -77.5390625 424.703125 -80.17578125Q422.1640625 -82.8125 417.18359375 -82.8125Q411.03125 -82.8125 407.125 -78.466796875Q403.21875 -74.12109375 401.36328125 -66.845703125Q399.5078125 -59.5703125 399.5078125 -50.68359375V0.0H365.328125V-64.453125Q365.328125 -69.23828125 364.400390625 -73.4375Q363.47265625 -77.63671875 360.884765625 -80.224609375Q358.296875 -82.8125 353.31640625 -82.8125Q347.1640625 -82.8125 343.2578125 -78.515625Q339.3515625 -74.21875 337.544921875 -66.943359375Q335.73828125 -59.66796875 335.73828125 -50.5859375V0.0Z"/>
<path style="fill:var(--wm-ly,#D0451A)" d="M507.546875 0.0Q493.58203125 0.0 486.6484375 -6.34765625Q479.71484375 -12.6953125 479.71484375 -25.1953125V-146.484375H513.9921875V-29.8828125Q513.9921875 -26.5625 514.919921875 -25.48828125Q515.84765625 -24.4140625 518.875 -24.4140625H526.1015625V0.0Z"/>
<path style="fill:var(--wm-ly,#D0451A)" d="M541.953125 38.0859375V13.671875H560.5078125Q562.65625 13.671875 563.73046875 12.890625Q564.8046875 12.109375 565.68359375 9.86328125L570.17578125 -2.05078125L568.515625 9.765625L521.15234375 -105.46875H559.43359375L584.140625 -25.09765625L581.50390625 -25.29296875L606.11328125 -105.46875H644.39453125L595.859375 18.45703125Q591.3671875 29.98046875 583.701171875 34.033203125Q576.03515625 38.0859375 565.29296875 38.0859375Z"/>
</g></symbol>
</defs></svg>'''

CSS = '''
:root{--navy-900:#1E3FA6;--navy-700:#142A70;--rule-dw:rgba(255,255,255,.11);--paper:#F3F6FB;--paper-2:#E6EDF8;--card:#FFFFFF;--rule-l:#D7DFEC;
  --ink:#0B1A33;--slate:#4A5B78;--snow:#EEF2FB;--mist:#C3D0F2;--electric:#DCE6FA;--link:#1E3FA6;--orange:#D0451A;--orange-deep:#B83A14;
  --display:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;--text:"Instrument Sans",-apple-system,"Segoe UI",system-ui,sans-serif;
  --r-ctl:10px;--wrap:1120px;--gutter:24px;--ease:cubic-bezier(.2,.7,.2,1);color-scheme:light}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 var(--text);overflow-x:hidden}
::selection{background:var(--link);color:#fff}:focus-visible{outline:2px solid var(--link);outline-offset:3px;border-radius:4px}
.nav :focus-visible{outline-color:var(--electric)}a{color:inherit}img,svg{display:block;max-width:100%}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 var(--gutter)}
h1,h2,h3{font-family:var(--display);letter-spacing:-.025em;line-height:1.08;margin:0;text-wrap:balance;font-variation-settings:"opsz" 96}
h1{font-size:clamp(2rem,4.4vw,3.2rem);font-weight:800;letter-spacing:-.035em;color:#fff}
h2{font-size:1.35rem;font-weight:700;letter-spacing:-.02em;margin:40px 0 10px;font-variation-settings:"opsz" 32}
h2:first-child{margin-top:0}
p{margin:0 0 12px}ul,ol{margin:0 0 12px;padding-left:22px}li{margin:4px 0}
.muted{color:var(--slate)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 22px;border-radius:var(--r-ctl);font-weight:600;font-size:1rem;text-decoration:none;border:1px solid transparent;cursor:pointer;line-height:1.2;white-space:nowrap;transition:transform .25s var(--ease),background .25s var(--ease)}
.btn.primary{background:var(--orange);color:#fff;box-shadow:0 1px 0 rgba(255,255,255,.18) inset,0 0 0 1px rgba(255,255,255,.32),0 8px 24px -10px rgba(11,26,51,.6)}
.btn.primary:hover{background:var(--orange-deep);transform:translateY(-1px)}
.btn.quiet{color:var(--snow);border-color:rgba(255,255,255,.28);background:rgba(255,255,255,.02)}.btn.quiet:hover{border-color:rgba(255,255,255,.6)}
.btn.small{padding:9px 14px;font-size:.92rem}
.lnk{color:var(--link);font-weight:600;text-decoration:none;background:linear-gradient(currentColor,currentColor) no-repeat 0 100%/0 1px;transition:background-size .3s var(--ease)}.lnk:hover{background-size:100% 1px}
.nav{position:sticky;top:0;z-index:50;background:#0B1A33}.nav .in{display:flex;align-items:center;justify-content:space-between;height:68px}
.brand{display:flex;align-items:center;text-decoration:none}.brand .wm{height:26px;width:auto}
.navlinks{display:flex;align-items:center;gap:26px;font-size:.95rem;color:var(--mist)}.navlinks a:not(.btn){text-decoration:none;transition:color .2s}.navlinks a:not(.btn):hover{color:#fff}
.navlinks .btn.quiet.small{border-color:rgba(255,255,255,.35)}
.hero{background:var(--navy-900);color:var(--snow);padding:56px 0 44px}
.hero .lead{color:var(--mist);max-width:60ch;margin:14px 0 0;font-size:1.05rem}
.hero .meta{color:var(--mist);font-size:.9rem;margin-top:14px}
.hero .meta a{color:var(--electric)}
main.legal{padding:48px 0 80px}
article{max-width:76ch}
article p,article li{color:var(--ink)}
article .note{background:var(--paper-2);border-left:3px solid var(--link);padding:12px 16px;border-radius:0 10px 10px 0;margin:16px 0}
article a{color:var(--link)}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:14px 0 18px;background:var(--card);border:1px solid var(--rule-l);border-radius:14px}
table{width:100%;border-collapse:collapse;font-size:.95rem;min-width:560px}
td,th{text-align:left;padding:11px 14px;border-bottom:1px solid var(--rule-l);vertical-align:top}
tr:last-child td{border-bottom:0}th{font:600 .8rem var(--text);color:var(--slate);white-space:nowrap;background:var(--paper)}
.toc{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:.92rem;margin:0 0 28px;padding:0;list-style:none}
.toc a{color:var(--link);text-decoration:none}.toc a:hover{text-decoration:underline}
.operator{margin-top:48px;padding-top:20px;border-top:1px solid var(--rule-l);color:var(--slate);font-size:.95rem}
footer{background:#0B1A33;border-top:1px solid rgba(255,255,255,.12);padding:36px 0 28px;color:var(--mist);font-size:.9rem}
footer .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:24px}
footer b{display:block;color:#fff;margin-bottom:8px;font-family:var(--display);font-weight:700}
footer a,footer span{display:block;color:var(--mist);text-decoration:none;margin:5px 0;transition:color .2s}footer a:hover{color:#fff}
footer .bottom{border-top:1px solid var(--rule-dw);margin-top:26px;padding-top:16px;font-size:.84rem;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.nf{min-height:70vh;display:grid;place-items:center;text-align:center;padding:64px 0}
.nf h1{color:var(--ink);font-size:clamp(2.4rem,7vw,4.5rem)}.nf p{color:var(--slate);max-width:44ch;margin:14px auto 24px}
.nf .row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}.nf .btn.quiet{color:var(--ink);border-color:rgba(11,26,51,.3)}
@media (max-width:1000px){footer .cols{grid-template-columns:1fr 1fr}}
@media (max-width:640px){:root{--gutter:16px}body{font-size:16px}.nav .in{height:60px}.navlinks{gap:14px}.navlinks a:not(.btn){display:none}.hero{padding:36px 0 30px}main.legal{padding:32px 0 56px}footer .cols{grid-template-columns:1fr}h2{margin-top:30px}}
'''

NAV = '''<header class="nav" id="nav"><div class="wrap in">
  <a class="brand" href="/" aria-label="Kalmly home"><svg class="wm" viewBox="0 0 660 190" style="--wm-k:#F3F6FB;--wm-ly:#D0451A" width="90" height="26"><use href="#wm"/></svg></a>
  <nav class="navlinks" aria-label="Main"><a href="/#morning">How it works</a><a href="/pricing/">Pricing</a><a href="/login">Log in</a><a class="btn quiet small" href="/start">Start free</a></nav>
</div></header>'''

FOOTER = '''<footer><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="/" aria-label="Kalmly"><svg class="wm" viewBox="0 0 660 190" style="--wm-k:#F3F6FB;--wm-ly:#D0451A" width="90" height="26"><use href="#wm"/></svg></a><span style="margin-top:12px;max-width:30ch">Meta tells you what happened. Kalmly tells you what to do.</span><span style="max-width:30ch">Meta ads, planned and judged on your shop's sales.</span></div>
    <div><b>Product</b><a href="/#morning">How it works</a><a href="/pricing/">Pricing</a><a href="/demo/">Demo dashboard</a><a href="/login">Log in</a><a href="/start">Start free</a></div>
    <div><b>Company</b><span>Built in Amsterdam, founded 2026</span><a href="mailto:hello@kalmly.io">hello@kalmly.io</a><a href="https://www.linkedin.com/company/kalmly-io" rel="noopener noreferrer">LinkedIn</a></div>
    <div><b>Legal</b><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/dpa/">Data processing</a></div>
  </div>
  <div class="bottom"><span>© 2026 Kalmly · <a href="mailto:hello@kalmly.io" style="display:inline;margin:0">hello@kalmly.io</a></span><span>Meta tells you what happened. Kalmly tells you what to do.</span></div>
</div></footer>
<script>
(function(){var h=location.hostname;if(h.endsWith("kalmly.io")&&h.indexOf("app.")!==0||h.endsWith("github.io")){document.querySelectorAll('a[href^="/start"],a[href^="/login"]').forEach(function(a){a.href="https://app.kalmly.io"+a.getAttribute("href");});}})();
</script>'''


def shell(path, title, desc, hero_h1, hero_lead, body, noindex=False, canonical=None):
    canonical = canonical or ("https://kalmly.io/" + path.strip("/") + "/" if path != "404.html" else "https://kalmly.io/404.html")
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Kalmly</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">{robots}
<link rel="icon" type="image/png" sizes="64x64" href="/favicon.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=2">
<meta name="theme-color" content="#0B1A33">
<meta property="og:type" content="website"><meta property="og:site_name" content="Kalmly"><meta property="og:title" content="{title} — Kalmly"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://kalmly.io/og.png"><meta property="og:url" content="{canonical}">
<link rel="preload" href="/fonts/bricolage-var-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/instrument-var-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<style>{CSS}</style>
</head>
<body>
{WM}
{NAV}
<main class="legal">
<section class="hero"><div class="wrap"><h1>{hero_h1}</h1>{('<p class="lead">' + hero_lead + '</p>') if hero_lead else ''}<p class="meta">Last updated {UPDATED} · <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/dpa/">Data processing</a></p></div></section>
<div class="wrap"><article style="padding-top:40px">
{body}
</article></div>
</main>
{FOOTER}
</body>
</html>
'''


PRIVACY = f'''
<ul class="toc">
<li><a href="#what">What Kalmly is</a></li><li><a href="#data">What we collect</a></li><li><a href="#others">Data about your customers</a></li><li><a href="#basis">Legal basis</a></li><li><a href="#who">Who processes it for us</a></li><li><a href="#transfers">Transfers outside the EU</a></li><li><a href="#keep">How long we keep it</a></li><li><a href="#rights">Your rights</a></li><li><a href="#security">Security</a></li><li><a href="#cookies">Cookies</a></li><li><a href="#contact">Contact and complaints</a></li>
</ul>

<h2 id="what">What Kalmly is</h2>
<p>Kalmly reads a business's Meta (Facebook and Instagram) advertising data and, if the business connects it, its real results: shop orders, bookings, leads or website visits. From that it writes a first look at the account, a short morning update every day, answers to your questions in a chat, and a list of concrete actions. By default it only reads. If you switch on approvals, it makes one change in your ad account only after you tap Approve on that specific change.</p>

<h2 id="data">What we collect, and why</h2>
<div class="tablewrap"><table>
<tr><th>Data</th><th>Why</th><th>Kept</th></tr>
<tr><td>Your email address, business name, website, what you sell, and the settings you enter (your goal in your own words and the kind of goal: sales, bookings, leads, visits or sign-ups; target return; break-even; spending ceiling; segments; language; delivery preferences)</td><td>To run your account, translate your goal into numbers and judge your ads against it</td><td>Until you delete your account</td></tr>
<tr><td>Meta ads data: spend, delivery and result figures per campaign, ad set and ad; names; creatives (format, captions, thumbnails); learning status; change history; billing and balance status; if you connect it, your Instagram page's own posts and their likes, saves and comments</td><td>To write the first look, the morning update and the actions, and to answer your questions</td><td>Daily summaries for 13 months; raw reads are not kept beyond the day's check</td></tr>
<tr><td>Result data you connect: order date, order total and product names from your shop (Wix, Shopify, WooCommerce, Squarespace, Webflow, BigCommerce, Stripe, Mollie, PayPal, or sent from your own site); bookings; leads from Meta's lead forms, a form event on your website or a CRM such as HubSpot; or a weekly number you type in yourself</td><td>To judge ads on real results instead of Meta's estimates</td><td>Order and lead lines for 60 days; daily totals for 13 months</td></tr>
<tr><td>Connection keys you give us (read-only API keys, or a Facebook login permission; an edit permission only if you switch on approvals)</td><td>To read the data above, and, with approvals on, to make the change you tapped</td><td>Encrypted at rest; revoked the moment you disconnect, deleted with your account</td></tr>
<tr><td>Your chat: the questions you ask and the answers, and the morning messages</td><td>So you can read them back, and so answers have context</td><td>13 months</td></tr>
<tr><td>The actions log: every suggestion, whether you approved it, marked it done yourself or let it expire, and what the numbers did afterwards</td><td>To follow up each change on the right day and to improve the advice</td><td>Per account for 13 months; aggregated counts without your name or numbers may be kept longer</td></tr>
<tr><td>Payment details</td><td>Handled by Stripe; we store only Stripe's customer and subscription IDs</td><td>Per Stripe's policy</td></tr>
<tr><td>Telegram chat ID (only if you link Telegram)</td><td>To send the morning message there and answer questions</td><td>Until you unlink or delete</td></tr>
<tr><td>Technical logs (requests, errors, IP address)</td><td>To keep the service running and secure</td><td>30 days</td></tr>
</table></div>
<p>We do not use your data for advertising, we do not sell it, and we do not use it to train AI models.</p>

<h2 id="others">Data about your customers</h2>
<p>Order, booking and lead data may show what your customers bought or asked for. We ask your shop and your lead source only for the fields we need (date, amount, product or form name) and never for your customers' names, addresses or payment details. Where a lead source gives us more than that (a CRM record, for instance), we keep only the fields above. For this data you are the controller and Kalmly is your processor; the <a href="/dpa/">data processing agreement</a> covers it. You are responsible for mentioning Kalmly in your own privacy notice if your law requires it.</p>

<h2 id="basis">Legal basis</h2>
<p>Performing our contract with you (running your account and writing your checks) and our legitimate interest in keeping the service secure and improving it. Where we rely on your consent (linking Telegram, reading your Instagram posts, anonymous benchmarks), you can withdraw it at any time from your page.</p>
<p><b>Benchmarks.</b> We may show you anonymous medians across many Kalmly customers (for example a typical click rate for shops of a similar size). No business can be identified from them; a median is only produced from a group of at least ten businesses.</p>

<h2 id="who">Who processes your data for us</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>Role</th><th>Where</th></tr>
<tr><td>Our hosting provider</td><td>Runs the service and stores your data</td><td>European Union</td></tr>
<tr><td>Anthropic</td><td>The AI model that writes the words of each check and chat answer; it receives the numbers for that one check and does not use them to train models, under our agreement</td><td>United States</td></tr>
<tr><td>Stripe</td><td>Payments and subscriptions</td><td>EU and US, under Stripe's safeguards</td></tr>
<tr><td>Resend</td><td>Sends your login links and emails</td><td>European Union (Ireland)</td></tr>
<tr><td>Telegram</td><td>Delivers the morning message, only if you link it</td><td>Outside the EU</td></tr>
<tr><td>Meta, your shop platform, your lead source</td><td>We read from them with the keys you give us; we send nothing to them, except the change you tapped with approvals on</td><td>Per their own policies</td></tr>
</table></div>
<p>Each provider is bound by a data processing agreement. We give 30 days' notice by email before adding or changing a provider.</p>

<h2 id="transfers">Transfers outside the EU</h2>
<p>Your data is stored in the EU. Anthropic (US) receives the numbers of each check while it writes the words, under the EU standard contractual clauses and, where it applies, the EU–US Data Privacy Framework. Stripe and Telegram apply their own published safeguards. Nothing else leaves the EU.</p>

<h2 id="keep">How long we keep it</h2>
<p>As in the table above. When you delete your account, your settings, checks, chat, actions and keys are removed within 24 hours and backups are overwritten within 30 days. When you disconnect an ad account or a shop, its key is revoked immediately and the summaries already written stay until you delete the account.</p>

<h2 id="rights">Your rights</h2>
<p>You can see, correct, export or delete your data at any time: most of it from your own Kalmly page ("Delete my account" is there), the rest by emailing hello@kalmly.io. You can disconnect your ad account or shop at any moment, from your page or from Meta's Business Settings. You can object to processing based on our legitimate interest, and you can withdraw consent where we rely on it. We answer within 30 days.</p>

<h2 id="security">Security</h2>
<p>Connection keys and settings are encrypted at rest; all traffic is encrypted in transit; access to the servers is limited to the people who run Kalmly, with two-factor login. One customer can never see another customer's accounts or numbers. Your personal page link is your login: keep it private, and ask for a new one from the login page if it has been shared. If a breach ever affects your data, we tell you within 72 hours of learning about it.</p>

<h2 id="cookies">Cookies</h2>
<p>kalmly.io sets no cookies and loads no analytics or advertising trackers. The app sets no cookies either: your page link is your login. Fonts are served from kalmly.io itself. That is why there is no cookie banner.</p>

<h2 id="contact">Contact and complaints</h2>
<p>Questions or requests about your data: <a href="mailto:hello@kalmly.io">hello@kalmly.io</a>. If you are not satisfied with our answer, you can complain to the Dutch data protection authority, the <a href="https://www.autoriteitpersoonsgegevens.nl/" rel="noopener noreferrer">Autoriteit Persoonsgegevens</a>, or to the authority in your own EU country.</p>
<p>If we change this policy in a way that matters, we email you first.</p>

<p class="operator">Kalmly is operated by {OPERATOR}</p>
'''

TERMS = f'''
<ul class="toc">
<li><a href="#service">The service</a></li><li><a href="#account">Your account</a></li><li><a href="#trial">Trial, price and payment</a></li><li><a href="#cancel">Cancelling</a></li><li><a href="#approve">Approve-to-apply</a></li><li><a href="#advice">Advice, not a guarantee</a></li><li><a href="#fair">Fair use</a></li><li><a href="#data">Your data</a></li><li><a href="#end">Ending the service</a></li><li><a href="#law">Law</a></li><li><a href="#operator">Operator</a></li>
</ul>

<h2 id="service">The service</h2>
<p>Kalmly gives you a first look at your Meta ad account, a short update every morning, answers to your questions, and concrete actions, all judged on the real results you connect (shop orders, bookings, leads or website visits) and on the goal you set. It is advice, generated automatically from your numbers. You decide what to do with it.</p>

<h2 id="account">Your account</h2>
<p>One account per business, used by the people who run that business. Your personal page link is your login; you are responsible for keeping it private. You must have the right to connect the ad account, shop or lead source you connect, and the right to accept these terms on behalf of your business.</p>

<h2 id="trial">Trial, price and payment</h2>
<p>You enter a card when you sign up. The first 7 days are free. We email you on day 6. If you have not cancelled by the end of day 7, the plan you picked is charged on day 8 and renews every month, or every year if you chose yearly, until you cancel. Prices are shown on kalmly.io and at checkout and exclude VAT; VAT is added at checkout where it applies. Payment is handled by Stripe. If we change a price, we email you at least 30 days before it applies to you; you can cancel before then.</p>

<h2 id="cancel">Cancelling</h2>
<p>You can cancel at any time from your page ("Manage subscription"), with no notice period and no email to anyone. Cancel during the trial and nothing is charged. Cancel later and the subscription ends at the end of the period you have paid for; there is no refund for the remaining days of a started period, except where the law gives you one. Upgrades apply immediately; downgrades at the next renewal.</p>

<h2 id="approve">Approve-to-apply</h2>
<p>If you switch on approvals, Kalmly makes a change in your ad account only after you tap Approve on that specific change, on your instruction. Each suggestion is re-checked against your live numbers at the moment you tap, and the change is made exactly as shown: one change a day, never more than 20% on a budget, never on an ad set edited in the last 3 days or still learning, never pausing or editing a live ad, never switching on something that spends, and nothing while a balance or payment alert is open. A suggestion expires after 24 hours. You can undo any change in Ads Manager, switch approvals off, or remove Kalmly's permission in Meta Business Settings at any time. Kalmly is not responsible for the results of approved changes, for Meta changing its systems, or for changes you made yourself in between.</p>

<h2 id="advice">Advice, not a guarantee</h2>
<p>We work to keep the service available every day and to base every check on the latest data we can read. We cannot promise results: advertising outcomes depend on your market, your creatives, Meta's systems and your decisions. The goal you set is a target, not a promise. Kalmly is not liable for business losses, lost profit or decisions you take. Our total liability to you is limited to the amount you paid us in the twelve months before the claim, except for damage caused intentionally or by gross negligence, where the law does not allow a limit.</p>

<h2 id="fair">Fair use</h2>
<p>Each plan covers the ad accounts, shops and question volume stated on the pricing page. We may slow down or pause an account that uses the service in a way that harms it or other customers, or that breaks Meta's or your platform's terms. You may not resell the service or share one account between unrelated businesses.</p>

<h2 id="data">Your data</h2>
<p>Your data stays yours. How we handle it is described in the <a href="/privacy/">privacy policy</a>; for the data about your own customers that passes through Kalmly, the <a href="/dpa/">data processing agreement</a> applies. Both are part of these terms.</p>

<h2 id="end">Ending the service</h2>
<p>You can delete your account at any time from your page. We may end the service with 30 days' notice, refunding any prepaid period beyond that date, or immediately if these terms are seriously breached.</p>

<h2 id="law">Law</h2>
<p>Dutch law applies. Disputes go to the competent court in Amsterdam, unless the law gives you the right to another court. If a part of these terms turns out to be invalid, the rest stays in force.</p>

<h2 id="operator">Operator</h2>
<p>Kalmly is a service of {OPERATOR}</p>
'''

DPA = f'''
<p class="note">This agreement applies automatically between you (the customer) and Kalmly from the moment you accept the <a href="/terms/">terms of service</a>. It covers the personal data of <em>your</em> customers that passes through Kalmly, as required by article 28 of the GDPR. You do not need to sign anything; if your company needs a signed copy, email hello@kalmly.io.</p>

<h2>1. Roles</h2>
<p>For the data about your customers that you connect (order lines, bookings, lead records), you are the controller and Kalmly is your processor. For your own account data (your email, settings, chat), Kalmly is the controller, and the <a href="/privacy/">privacy policy</a> applies.</p>

<h2>2. Subject matter, duration, nature and purpose</h2>
<p>Kalmly processes the data on your instruction, for as long as your account exists, for one purpose: to judge your advertising on your real results and to write the first look, the morning update, the chat answers and the actions. Nothing else.</p>

<h2>3. Types of data and people concerned</h2>
<p>From your shop, booking tool or lead source: the date, the amount, the product, service or form name, and, for leads, the fact that a lead arrived and from which ad. The people concerned are your customers and the people who enquired with you. We do not request names, addresses, emails, phone numbers or payment details, and where a source sends more than we asked, we keep only the fields above.</p>

<h2>4. Your instructions</h2>
<p>Your instructions are these terms, the settings on your page and the connections you make. We process the data only on those instructions, unless EU or Dutch law requires otherwise, in which case we tell you first where the law allows it. If we think an instruction breaks the law, we tell you.</p>

<h2>5. Confidentiality</h2>
<p>Only the people who run Kalmly can access the servers, each bound to confidentiality, and only when it is needed to run or support the service.</p>

<h2>6. Security</h2>
<p>Encryption at rest for keys and settings; encryption in transit for all traffic; hosting in the EU; access limited to named people with two-factor login; separation between customers so one can never see another's data; daily backups; logs kept for 30 days. We tell you without undue delay, and at the latest within 72 hours of learning about it, if a breach affects your data, with what we know and what we are doing.</p>

<h2>7. Sub-processors</h2>
<p>You authorise the providers listed in the <a href="/privacy/#who">privacy policy</a>: our EU hosting provider, Anthropic (the words of each check; no training on your data), Stripe (payments), Resend (email), Telegram (only if you link it). Each is bound by a written agreement with at least these obligations. We email you 30 days before adding or replacing one; if you object on reasonable grounds and we cannot resolve it, you can end the service and we refund any prepaid period beyond that date.</p>

<h2>8. Help with your obligations</h2>
<p>If one of your customers asks you about their data, we help you find, correct, export or delete it within 10 working days. We help you with data protection impact assessments and with the authorities, as far as it concerns Kalmly's processing.</p>

<h2>9. Transfers outside the EU</h2>
<p>Your customers' data is stored in the EU. Anthropic (US) receives the numbers of each check, not individual order or lead lines, under the EU standard contractual clauses and, where it applies, the EU–US Data Privacy Framework.</p>

<h2>10. Deletion and return</h2>
<p>Disconnect a source and its key is revoked immediately. Delete your account and the data is removed within 24 hours and from backups within 30 days. On request before deletion, we export your data in a common format.</p>

<h2>11. Audits</h2>
<p>Once a year, on 30 days' written notice, you may ask us for the information needed to show we meet this agreement, or have an independent auditor bound by confidentiality review it at your cost, in a way that does not disrupt the service or expose other customers' data.</p>

<h2>12. Liability and law</h2>
<p>The liability limits, the law and the court in the <a href="/terms/">terms of service</a> apply to this agreement. It is governed by Dutch law and the GDPR.</p>

<p class="operator">Processor: {OPERATOR}</p>
'''

NOT_FOUND = '''
<div class="nf"><div>
<p class="muted" style="font-size:.85rem;letter-spacing:.12em;text-transform:uppercase">404</p>
<h1>That page is not here.</h1>
<p>The link may be old, or mistyped. Everything that matters is one click away.</p>
<div class="row"><a class="btn primary" href="/">Go to the homepage</a><a class="btn quiet" href="/demo/">See the demo</a></div>
</div></div>
'''


def write(rel, html):
    p = HERE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html)
    print("wrote", rel, len(html))


write("privacy/index.html", shell("privacy", "Privacy policy",
      "How Kalmly handles your data: what it reads from Meta and your shop, why, how long it keeps it, who processes it, and your rights. No cookies.",
      "Privacy policy", "What Kalmly reads, why, how long it keeps it, and your rights. In plain words.", PRIVACY))
write("terms/index.html", shell("terms", "Terms of service",
      "Kalmly's terms: the 7-day trial, billing, cancelling any time from your page, approve-to-apply rules, and what Kalmly does and does not promise.",
      "Terms of service", "The trial, the price, cancelling, and what Kalmly does and does not promise.", TERMS))
write("dpa/index.html", shell("dpa", "Data processing agreement",
      "Kalmly's data processing agreement (GDPR article 28) for business customers: roles, data, security, sub-processors, deletion and audits.",
      "Data processing agreement", "For the data about your customers that passes through Kalmly. Applies automatically with the terms.", DPA))

# 404: a plain paper page, no hero band
nf = shell("404.html", "Page not found", "This page does not exist on kalmly.io.", "", "", "", noindex=True)
nf = nf.replace('<section class="hero">', '<section class="hero" hidden>').replace('<article style="padding-top:40px">\n\n</article>', '<div>' + NOT_FOUND + '</div>')
write("404.html", nf)
