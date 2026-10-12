# -*- coding: utf-8 -*-
"""Generates the static pages for scotkenneyacquisitions.com from the
October 2026 redesign brief. Run from the repo root:  python tools/build_pages.py
All page copy below is the brief's approved copy, verbatim."""
import os, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "Scot Kenney Acquisitions"
EMAIL = "Scot@scotkenneyacquisitions.com"
PHONE_DISPLAY = "+1 530-415-0778"
PHONE_TEL = "+15304150778"
WHATSAPP = "https://wa.me/15304150778"
# Leave empty until a form-relay endpoint (e.g. Formspree) is created in Scot's name.
FORM_ENDPOINT = "https://formsubmit.co/ajax/Scot@scotkenneyacquisitions.com"  # no-account relay; first submission triggers a one-time activation email to Scot

# Illustrative stock imagery (Unsplash License) plus local images/. Sources and licenses: IMAGE_SOURCES.md
U = "https://images.unsplash.com/photo-{id}?auto=format&fit=crop&w={w}&q={q}"
def img(id_, w=1600, q=70): return U.format(id=id_, w=w, q=q)
IMG = {
    "hero":        "images/hero-waterfront-ai.jpg",                      # AI candidate, labeled "Conceptual illustration"
    "multifamily": img("1580041065738-e72023775cdc", 1200),             # KEEP (owner instruction)
    "yacht":       img("1567899378494-47b22a2ae96a", 1200),             # KEEP on Property Focus (owner instruction)
    "rv":          "images/owner-motorcoach-clubhouse-concept.jpg",      # owner-supplied Image A
    "residential": "images/concept-community-entrance.jpg",              # owner-supplied Vue entrance rendering
    "approach":    "images/marina-aerial.jpg",                           # owner's original Expertise-page marina aerial
    "marina":      img("1730402733045-269e1b446856", 1200),             # home waterfront card (scan item 3)
    "coachsite":   "images/motorcoach-site-illustrative.jpg",            # PF RV image (scan item 2)
    "lavender":    "images/owner-blackfoot-lavender-retreat-concept.jpg",# owner-supplied Image B
}
def P(r, key):
    """Image URL for a page at depth r; local files under images/ need the relative prefix."""
    v = IMG[key]
    return v if v.startswith("http") else r + v

NAV = [("Home", ""), ("Approach", "approach/"), ("Property Focus", "property-focus/"), ("About", "about/"), ("Contact", "contact/")]

MARK = """<svg class="brand-mark" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 40h40"/><path d="M8 40V26h7v14"/><path d="M18 40V18h8v22"/><path d="M29 40V12h8v28"/><path d="M33 12V5"/><path d="M33 7l6 3-6 3"/><path d="M11 30h1M11 34h1M21 23h2M21 28h2M21 33h2M32 18h2M32 24h2M32 30h2M32 36h2"/></g></svg>"""
ARROW = """<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
FAVICON = "data:image/svg+xml," + ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'><rect width='48' height='48' fill='%230f1f33'/><g fill='none' stroke='%23d9c9a3' stroke-width='2' stroke-linecap='round'><path d='M6 40h36'/><path d='M10 40V26h7v14'/><path d='M20 40V18h8v22'/><path d='M31 40V12h8v28'/><path d='M35 12V6'/></g></svg>").replace("#", "%23")

NOTICE = ("This website provides general information about Scot Kenney Acquisitions and its business interests. "
          "It is not an offer to sell or a solicitation of an offer to buy securities.")

def head(r, title, desc, current):
    full = SITE if current == "" else f"{title} | {SITE}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="color-scheme" content="light only">
<meta name="darkreader-lock">
<meta name="theme-color" content="#0f1f33">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/style.css?v=6">
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r if r else './'}" aria-label="{SITE} home">
      {MARK}
      <span class="brand-text"><span class="brand-name">Scot Kenney</span><span class="brand-sub">Acquisitions</span></span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {nav_links(r, current)}
    </nav>
  </div>
</header>
<main id="main">
"""

def nav_links(r, current):
    out = []
    for label, path in NAV:
        href = (r + path) if path else (r if r else "./")
        cur = ' aria-current="page"' if path == current else ""
        cls = ' class="nav-cta"' if path == "contact/" else ""
        out.append(f'<a href="{href}"{cur}{cls}>{label}</a>')
    return "\n      ".join(out)

def foot(r):
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="brand" href="{r if r else './'}">{MARK}<span class="brand-text"><span class="brand-name">Scot Kenney</span><span class="brand-sub">Acquisitions</span></span></a>
        <p style="margin-top:1.2rem;max-width:40ch">Strategic real estate acquisitions, development, and partnerships.</p>
      </div>
      <div>
        <h4>Navigate</h4>
        <ul>
          <li><a href="{r if r else './'}">Home</a></li>
          <li><a href="{r}approach/">Approach</a></li>
          <li><a href="{r}property-focus/">Property Focus</a></li>
          <li><a href="{r}about/">About</a></li>
          <li><a href="{r}contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="{WHATSAPP}" rel="noopener">Call, text, or WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-notice">
      <p>{NOTICE} <a href="{r}website-notice/">Website Notice</a></p>
      <p>&copy; 2026 {SITE}</p>
    </div>
  </div>
</footer>
<script src="{r}js/main.js?v=2"></script>
</body>
</html>
"""

def cta_band(r, h, p, label, href):
    return f"""
<section class="cta-band">
  <div class="wrap">
    <div><h2>{h}</h2><p>{p}</p></div>
    <a class="btn btn-light" href="{r}{href}">{label} {ARROW}</a>
  </div>
</section>"""

# ----------------------------------------------------------------------------- HOME
def home():
    r = ""
    h = head(r, "Home", "Scot Kenney Acquisitions identifies distinctive real estate opportunities where thoughtful acquisitions, operational improvements, and creative development strategies may unlock long-term value.", "")
    body = f"""
<section class="hero hero-left">
  <div class="hero-media"><img src="{P(r, 'hero')}" alt="Conceptual illustration of a boutique waterfront apartment building with boats at its private dock" fetchpriority="high"></div>
  <div class="wrap">
    <p class="eyebrow">Scot Kenney Acquisitions</p>
    <h1>Strategic Real Estate Acquisitions &amp; Development</h1>
    <p class="sub">Identifying Opportunities. Creating Value. Building Strategic Partnerships.</p>
    <p class="lead">Scot Kenney Acquisitions identifies distinctive real estate opportunities where thoughtful acquisitions, operational improvements, and creative development strategies may unlock long-term value. Our interests span multifamily, waterfront properties, marinas, upscale RV resorts, and innovative residential communities.</p>
    <div class="btn-row">
      <a class="btn btn-light" href="approach/">Our Approach {ARROW}</a>
      <a class="btn btn-ghost" href="contact/">Start a Conversation</a>
    </div>
  </div>
  <span class="hero-note">Conceptual illustration</span>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Where We Focus</p>
      <h2>Selective interests, evaluated on their merits</h2>
    </div>
    <div class="grid-4">
      <article class="focus-card reveal">
        <div class="img"><img src="{P(r, 'multifamily')}" alt="Low-rise apartment community with landscaped courtyard" loading="lazy"><span class="img-tag">Illustrative imagery</span></div>
        <div class="body"><h3>Multifamily &amp; Income Properties</h3><p>From boutique properties to larger portfolios, we evaluate each acquisition on its merits, without arbitrary unit-count limits.</p></div>
      </article>
      <article class="focus-card reveal">
        <div class="img"><img src="{P(r, 'marina')}" alt="Aerial view of a marina beside waterfront residential buildings" loading="lazy"><span class="img-tag">Illustrative imagery</span></div>
        <div class="body"><h3>Waterfront &amp; Marina Opportunities</h3><p>Residential properties, dockage, marina-related assets, and other waterfront locations with multiple potential revenue sources.</p></div>
      </article>
      <article class="focus-card reveal">
        <div class="img"><img src="{P(r, 'rv')}" alt="Conceptual illustration of a luxury motorcoach resort with a three-story black-glass clubhouse and pool" loading="lazy"><span class="img-tag">Concept illustration</span></div>
        <div class="body"><h3>Distinctive RV Resorts</h3><p>Well-planned motorcoach and RV destinations emphasizing attractive environments, thoughtful amenities, and compelling guest experiences&mdash;not ordinary storage lots.</p></div>
      </article>
      <article class="focus-card reveal">
        <div class="img"><img src="{P(r, 'residential')}" alt="Concept illustration of the residential community entrance" loading="lazy"><span class="img-tag">Concept illustration</span></div>
        <div class="body"><h3>Innovative Residential Development</h3><p>Exploring modern, design-forward residential communities and adaptable development concepts.</p></div>
      </article>
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="reveal measure">
      <p class="eyebrow">How We Create Value</p>
      <h2>We look beyond the listing</h2>
      <p class="lead">We look beyond the listing to examine property economics, overlooked revenue opportunities, physical improvements, positioning, operations, and realistic exit options. Each project requires independent due diligence and a sound execution plan.</p>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="grid-2">
      <div class="reveal">
        <p class="eyebrow">Strategic Relationships</p>
        <h2>Conversations with established partners</h2>
      </div>
      <div class="reveal">
        <p class="lead" style="color:rgba(255,255,255,.82)">We welcome conversations with established family offices, private real estate capital firms, developers, and experienced operating partners. Relationships may involve individual acquisitions, joint ventures, or broader collaboration, depending on the opportunity.</p>
        <a class="btn btn-light" href="contact/?topic=capital">Discuss a Potential Partnership {ARROW}</a>
      </div>
    </div>
  </div>
</section>
"""
    return h + body + foot(r)

# ----------------------------------------------------------------------------- APPROACH
def approach():
    r = "../"
    h = head(r, "Approach", "An opportunity-driven acquisition philosophy: identify, underwrite, structure, execute, reassess.", "approach/")
    body = f"""
<section class="page-head bright">
  <div class="hero-media"><img src="{P(r, 'approach')}" alt="Aerial view of a marina with boats at the docks"></div>
  <div class="wrap">
    <p class="eyebrow">Approach</p>
    <h1>An Opportunity-Driven Acquisition Philosophy</h1>
  </div>
  <span class="hero-note">Illustrative imagery</span>
</section>

<section class="section">
  <div class="wrap">
    <p class="lead reveal" style="max-width:72ch">We pursue opportunities where the acquisition basis, property characteristics, and a practical operating or development plan create a compelling business case. We are not restricted by a minimum or maximum number of apartment units, a single property category, or a one-size-fits-all financing structure.</p>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Our Process</p><h2>Five disciplined steps</h2></div>
    <ol class="process">
      <li class="reveal"><h3>Identify</h3><p>Source properties and situations where pricing, location, management, design, or unrealized potential warrant closer study.</p></li>
      <li class="reveal"><h3>Underwrite</h3><p>Examine current income, realistic expenses, capital requirements, financing, regulations, and downside scenarios.</p></li>
      <li class="reveal"><h3>Structure</h3><p>Explore an appropriate acquisition and partnership structure for the specific property.</p></li>
      <li class="reveal"><h3>Execute</h3><p>Coordinate qualified local professionals and operating partners to implement the business plan.</p></li>
      <li class="reveal"><h3>Reassess</h3><p>Monitor results and consider refinancing, long-term ownership, or disposition as circumstances warrant.</p></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap grid-2">
    <div class="reveal"><p class="eyebrow">Partnering Philosophy</p><h2>Complementary relationships</h2></div>
    <div class="reveal"><p class="lead">We value complementary relationships with experienced, well-capitalized organizations. Depending on the transaction, a capital partner may provide equity, financing resources, operating capabilities, development expertise, or a combination of these. Roles and economics are negotiated separately for each transaction.</p></div>
  </div>
</section>
{cta_band(r, "Connect With Us", "Tell us about the opportunity or the relationship you have in mind.", "Connect With Us", "contact/")}
"""
    return h + body + foot(r)

# ----------------------------------------------------------------------------- PROPERTY FOCUS
def property_focus():
    r = "../"
    h = head(r, "Property Focus", "Selective across property types: multifamily and mixed-use, waterfront real estate and marinas, distinctive RV and motorcoach destinations, next-generation technology communities.", "property-focus/")
    body = f"""
<section class="page-head plain">
  <div class="wrap">
    <p class="eyebrow">Property Focus</p>
    <h1>Selective Across Property Types</h1>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="pf-item reveal">
      <div class="pf-media"><img src="{P(r, 'multifamily')}" alt="Low-rise apartment community with landscaped courtyard" loading="lazy"><span class="img-tag">Illustrative imagery</span></div>
      <div>
        <h2>Multifamily &amp; Mixed-Use</h2>
        <p>We consider income-producing residential properties of varying sizes, including smaller assets with unusual locations or compelling operational potential and larger acquisitions where scale creates efficiencies.</p>
      </div>
    </div>

    <div class="pf-item reveal">
      <div class="pf-media"><img src="{P(r, 'yacht')}" alt="Motor yacht moored along a tree-lined waterfront" loading="lazy"><span class="img-tag">Illustrative imagery</span></div>
      <div>
        <h2>Waterfront Real Estate &amp; Marinas</h2>
        <p>Waterfront apartments, marina assets, boat slips, and related properties may offer distinctive combinations of location, income, and repositioning possibilities. Every opportunity must be evaluated for local permitting, insurance, dockage rights, operating costs, and demand.</p>
      </div>
    </div>

    <div class="pf-item reveal" style="grid-template-columns:1fr">
      <div class="measure">
        <h2>Distinctive RV &amp; Motorcoach Destinations</h2>
        <p>We evaluate distinctive RV and motorcoach destinations where design, landscaping, hospitality, and amenities could create a compelling guest experience and additional revenue opportunities. As one example of our founder&rsquo;s creative approach, Scot Kenney conceived a luxury motorcoach resort with a dramatic three-story black-glass clubhouse, private-site amenities, dining, and cultural events; an architect prepared an illustration of his concept. This was a design concept, not a completed development.</p>
        <div class="pf-media" style="margin-top:1.6rem;max-width:560px"><img src="{P(r, 'coachsite')}" alt="Illustrative image of a luxury Class A motorcoach on a landscaped private site with a cabana and plunge pool" loading="lazy"><span class="img-tag">Illustrative imagery</span></div>
        <p class="muted" style="font-size:.88rem;margin-top:.6rem">Illustrative imagery; not a completed Scot Kenney Acquisitions project.</p>
      </div>
    </div>

    <div class="pf-item reveal">
      <div class="concept" style="margin:0">
        <figure>
          <div class="frame">{concept_slot("entrance")}</div>
          <figcaption><strong>Concept illustration</strong>Original development concept. Subject to feasibility and applicable approvals.</figcaption>
        </figure>
      </div>
      <div>
        <h2>Next-Generation Technology Communities</h2>
        <p>Exploring distinctive, technology-focused residential communities designed around the evolving lifestyles and requirements of professionals in artificial intelligence and other advanced industries.</p>
      </div>
    </div>

    <div class="pf-item reveal" style="grid-template-columns:1fr">
      <div class="measure">
        <h2>Additional Opportunities</h2>
        <p>We remain open to other real estate opportunities when the acquisition economics, execution requirements, and potential value creation justify consideration.</p>
      </div>
    </div>
  </div>
</section>
{cta_band(r, "Submit a Property Opportunity", "Owners and brokers: tell us about the property and what makes it distinctive.", "Submit a Property Opportunity", "contact/?topic=property")}
"""
    return h + body + foot(r)

def concept_slot(which):
    """Owner-supplied images only. If the file is present in images/, show it; otherwise a labeled placeholder."""
    files = {"motorcoach": "images/concept-motorcoach-resort.jpg", "entrance": "images/concept-community-entrance.jpg"}
    alt = {"motorcoach": "Architect's concept illustration of a luxury motorcoach resort clubhouse", "entrance": "Concept illustration of the residential community entrance"}
    path = files[which]
    if os.path.exists(os.path.join(ROOT, path)):
        return f'<img src="../{path}" alt="{alt[which]}" loading="lazy">'
    label = {"motorcoach": "Owner-supplied architect illustration to be placed here", "entrance": "Owner-supplied entrance rendering to be placed here"}[which]
    return f'<div class="placeholder"><div><strong>Image placeholder</strong>{label}<br><span class="muted">Awaiting the owner-provided file &mdash; no substitute imagery is used.</span></div></div>'

# ----------------------------------------------------------------------------- ABOUT
def about():
    r = "../"
    h = head(r, "About", "Entrepreneurial thinking. Disciplined real estate evaluation.", "about/")
    body = f"""
<section class="page-head plain">
  <div class="wrap">
    <p class="eyebrow">About</p>
    <h1>Entrepreneurial Thinking. Disciplined Real Estate Evaluation.</h1>
  </div>
</section>

<section class="section">
  <div class="wrap grid-2" style="align-items:start">
    <div class="reveal">
      <p class="eyebrow">Who We Are</p>
      <h2>Individual properties, evaluated on the opportunities they present</h2>
    </div>
    <div class="reveal">
      <p class="lead">Scot Kenney Acquisitions is guided by an entrepreneurial approach to identifying real estate opportunities and considering practical ways to improve their usefulness, appeal, and financial performance. Rather than relying on rigid acquisition categories, the company evaluates individual properties and the specific opportunities they present.</p>
      <p>Our interests range from conventional income-producing assets to distinctive waterfront and resort properties and new residential concepts. We recognize that successful execution depends on careful underwriting, appropriate financing, local market knowledge, and collaboration with qualified professionals.</p>
      <p>We seek productive relationships with property owners, commercial brokers, family offices, established capital firms, developers, and experienced operating organizations.</p>
    </div>
  </div>
</section>
<section class="section tint">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Creative Vision</p>
      <h2>Creative Vision. Real Estate Opportunity.</h2>
    </div>
    <figure class="feature reveal">
      <div class="split-media"><img src="{P(r, 'lavender')}" alt="Conceptual rendering of lavender fields, a fountain, a fire pit and a barn-style building at dusk" loading="lazy"><span class="img-tag">Conceptual rendering</span></div>
      <figcaption>Conceptual rendering: an illustrative vision of transforming land. Not a photograph of a completed company development.</figcaption>
    </figure>
  </div>
</section>
{cta_band(r, "Get in Touch", "We welcome a direct conversation about properties, capital relationships, or collaboration.", "Get in Touch", "contact/")}
"""
    return h + body + foot(r)

# ----------------------------------------------------------------------------- CONTACT
def contact():
    r = "../"
    h = head(r, "Contact", "Start a business conversation with Scot Kenney Acquisitions.", "contact/")
    body = f"""
<section class="page-head plain">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Start a Business Conversation</h1>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <p class="lead reveal">We welcome inquiries from established capital groups, family offices, real estate investment firms, property owners, commercial brokers, developers, and potential operating partners.</p>
      <form class="form reveal" id="contact-form" method="post" action="{FORM_ENDPOINT or '#'}" data-endpoint="{FORM_ENDPOINT}" data-destination="{EMAIL}" novalidate>
        <div class="row">
          <div class="field"><label for="f-name">Name <span class="req" aria-hidden="true">*</span></label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-org">Organization</label><input id="f-org" name="organization" type="text" autocomplete="organization"></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-email">Email <span class="req" aria-hidden="true">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="f-tel">Telephone <span class="muted">(optional)</span></label><input id="f-tel" name="telephone" type="tel" autocomplete="tel"></div>
        </div>
        <div class="field">
          <label for="f-topic">I am contacting you about <span class="req" aria-hidden="true">*</span></label>
          <select id="f-topic" name="topic" required>
            <option value="" selected disabled>Select one</option>
            <option value="Capital / Joint Venture Partnership">Capital / Joint Venture Partnership</option>
            <option value="Property for Sale">Property for Sale</option>
            <option value="Brokerage Opportunity">Brokerage Opportunity</option>
            <option value="Development Collaboration">Development Collaboration</option>
            <option value="Other">Other</option>
          </select>
        </div>
        <div class="field"><label for="f-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="f-msg" name="message" required></textarea></div>
        <input type="hidden" name="_subject" value="Website inquiry - scotkenneyacquisitions.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
        <div class="hp" aria-hidden="true"><label>Leave this field empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
        <div class="btn-row" style="align-items:center;gap:1.4rem">
          <button class="btn btn-primary" type="submit">Send Inquiry</button>
          <p class="form-note">Please do not send financial statements or confidential documents through this form.</p>
        </div>
        <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
      </form>
    </div>
    <aside class="contact-aside reveal">
      <h3>Direct contact</h3>
      <dl>
        <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>Telephone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
        <div><dt>Call, text, message</dt><dd><a href="{WHATSAPP}" rel="noopener">WhatsApp</a></dd></div>
      </dl>
    </aside>
  </div>
</section>
"""
    return h + body + foot(r)

# ----------------------------------------------------------------------------- WEBSITE NOTICE
def notice():
    r = "../"
    h = head(r, "Website Notice", "Website notice for scotkenneyacquisitions.com.", "website-notice/")
    body = f"""
<section class="page-head plain">
  <div class="wrap"><p class="eyebrow">Website Notice</p><h1>Website Notice</h1></div>
</section>
<section class="section">
  <div class="wrap prose">
    <p class="lead">{NOTICE}</p>
    <h2>Information on this site</h2>
    <p>Content on this website describes the general business interests of Scot Kenney Acquisitions. Property types, concepts, and illustrations are presented for informational purposes. Architectural renderings labeled &ldquo;Concept illustration&rdquo; depict design concepts only and do not represent completed projects, active developments, or current offerings. Images labeled &ldquo;Conceptual illustration&rdquo; or &ldquo;Conceptual rendering&rdquo; are renderings of concepts, not photographs of an existing, completed, or company-owned property. Photographs labeled &ldquo;Illustrative imagery&rdquo; are stock or archival images used for illustration and do not depict properties owned, operated, or acquired by the company.</p>
    <h2>Contact form</h2>
    <p>Information submitted through the contact form (name, organization, email address, telephone, and message) is used only to review and respond to your inquiry. It is sent to {EMAIL} and is not sold or shared with third parties. Please do not submit financial statements or confidential documents through the form.</p>
    <h2>Contact</h2>
    <p><a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
  </div>
</section>
"""
    return h + body + foot(r)

# ----------------------------------------------------------------------------- 404 + legacy redirects
def redirect_page(target_rel, label):
    # Client-side redirect for retired URLs (GitHub Pages has no server-side redirects).
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Redirecting | {SITE}</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{target_rel}">
<meta http-equiv="refresh" content="0; url={target_rel}">
<script>location.replace("{target_rel}");</script>
<style>body{{font-family:system-ui,sans-serif;padding:3rem;color:#1b1f24}}</style></head>
<body><p>This page has moved to <a href="{target_rel}">{label}</a>.</p></body></html>
"""

def not_found():
    r = "/scot-kenney-acquisitions/" if os.environ.get("STAGING") else "/"
    # 404 must use absolute paths because it is served from any depth.
    page = head(r, "Page not found", "The page you requested could not be found.", "404")
    body = f"""
<section class="page-head plain"><div class="wrap"><p class="eyebrow">404</p><h1>Page not found</h1></div></section>
<section class="section"><div class="wrap prose"><p class="lead">The page you requested could not be found. It may have moved as part of our website update.</p>
<a class="btn btn-primary" href="{r}">Return to the homepage {ARROW}</a></div></section>
"""
    return page + body + foot(r)

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with io.open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", path)

if __name__ == "__main__":
    write("index.html", home())
    write("approach/index.html", approach())
    write("property-focus/index.html", property_focus())
    write("about/index.html", about())
    write("contact/index.html", contact())
    write("website-notice/index.html", notice())
    write("404.html", not_found())
    # Retired URLs from the previous site -> new pages
    write("invest/index.html", redirect_page("../approach/", "Approach"))
    write("expertise/index.html", redirect_page("../property-focus/", "Property Focus"))
    write("disclosures/index.html", redirect_page("../website-notice/", "Website Notice"))
    write("terms/index.html", redirect_page("../website-notice/", "Website Notice"))
    write("robots.txt", "User-agent: *" + chr(10) + "Allow: /" + chr(10) + "Sitemap: https://www.scotkenneyacquisitions.com/sitemap.xml" + chr(10))
    base = "https://www.scotkenneyacquisitions.com/"
    urls = ["", "approach/", "property-focus/", "about/", "contact/", "website-notice/"]
    NL = chr(10)
    sm = '<?xml version="1.0" encoding="UTF-8"?>' + NL + '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + NL
    sm += "".join("  <url><loc>%s%s</loc></url>" % (base, u) + NL for u in urls) + "</urlset>" + NL
    write("sitemap.xml", sm)
    write(".nojekyll", "")
