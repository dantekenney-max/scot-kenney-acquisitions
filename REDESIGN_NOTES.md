# Scot Kenney Acquisitions — Website Redesign (October 2026)

Source brief: `Scot_Kenney_Acquisitions_Website_Redesign_REVISED.docx` (emailed by Scot, Sat 10/10/2026). This document is the authoritative content brief; this site implements it verbatim.

## Spec (locked 2026-10-11)

**GOAL.** Replace the current scotkenneyacquisitions.com (an investor-solicitation style site: "Passive Income Investing", 506(c), $200k minimum, 15-18% targets) with a sophisticated real estate acquisitions / development / strategic partnerships site aimed at family offices, private RE funds, JV partners, property owners and brokers. No offering language anywhere.

**INPUTS.** The brief's page copy (sections 4-8), its image/design direction (9), legal cleanup (10), checklist (11), creative-concept guidance (13). Two owner-supplied images emailed separately (architect illustration of the luxury motorcoach resort; the technology-community ENTRANCE rendering).

**OUTPUTS.** A static 5-page site (+ Website Notice + 404): HOME, APPROACH, PROPERTY FOCUS, ABOUT, CONTACT. Hosted on GitHub Pages as a **staging preview** at https://dantekenney-max.github.io/scot-kenney-acquisitions/ for owner approval. Nothing is published to the live domain until Scot approves.

**CONSTRAINTS.**
- Staging only; no automatic publish to the live domain (brief §2).
- Preserve: domain, email `Scot@scotkenneyacquisitions.com`, phone `530-415-0778`, brand identity (skyline mark + wordmark), mobile layout, working contact form.
- Remove entirely (not hide): 506(b)/506(c) language, $200,000 minimum, return targets, accreditation questions, "Investor Sign in", stale investor forms, duplicate disclaimers.
- No invented credentials, partnerships, projects, track record, bios.
- Illustrative stock imagery labeled as such; renderings labeled "Concept illustration".
- Do not mention Blackfoot Lavender Retreat. Do not reveal technology-community design details beyond the approved copy.

**DONE = observable on Dante's screen.**
1. Staging URL loads all 5 pages + Website Notice with no console errors, desktop and mobile widths.
2. Every page uses the brief's approved copy word-for-word and has exactly one primary CTA.
3. A site-wide text search finds zero hits for: `506`, `$200,000`, `accredited`, `Investor Sign in`, `15%`, `18%`, `Sponsor Name`, `Lavender`.
4. Nav = HOME | APPROACH | PROPERTY FOCUS | ABOUT | CONTACT, footer link WEBSITE NOTICE; old URLs `/invest`, `/expertise`, `/disclosures` redirect to the new pages.
5. Contact form has the brief's fields (Name*, Organization, Email*, Telephone, "I am contacting you about" select, Message*), spam honeypot, and the brief's confirmation message.
6. Footer carries the brief's short notice verbatim.
7. The two owner-supplied images appear only where the brief allows (Property Focus), with the approved captions; until those files are copied in, clearly labeled placeholders appear instead.

**NON-GOALS.** Not touching the live domain / DNS / Bluehost / email in this pass. No CMS. No analytics unless the current site's analytics ID is confirmed (none was visible on the live pages).

## Approach + spike (Phase 1)

| Approach | Tradeoff | Confidence |
|---|---|---|
| **A. Static HTML/CSS on GitHub Pages, then flip Bluehost DNS** (same path already proven for blackfootlavenderretreat.com) | Form needs a free form-relay (Formspree) — a 1-minute account that Scot or Dante owns | 90% |
| B. Edit the existing site in place on Bluehost (looks like a page-builder/WordPress install) | Needs Scot's Bluehost login + email 2FA every session; easy to break email/DNS; hard to remove the old offering text cleanly | 40% |
| C. Upload static site to Bluehost hosting + PHP mail form | Same login wall as B | 55% |

Front-runner A. Riskiest assumption: a new repo + Pages can be created and served right now via the API token. **Spike ran 2026-10-11 16:10 ET:** repo `dantekenney-max/scot-kenney-acquisitions` created, placeholder pushed, Pages enabled, URL returned HTTP 200 within ~30 s. GREEN.

## Current live site inventory (captured 2026-10-11, before any change)

Host: Bluehost (A record 67.20.76.83, Apache; the same Bluehost account that holds blackfootlavenderretreat.com). Page title "Passive Income Investing".

| Old URL | Content | New disposition |
|---|---|---|
| `/` | "A Multifamily, Storage, Marina, and Off Shore Resorts Real Estate Investment Company", "LEVEL-UP YOUR LEGACY", risk disclosure, 506(c) $200k paragraph | Replaced by new HOME |
| `/invest` | "Why Invest?" — Strong Returns / Stability / Tax Benefits / Buy Criteria / Risk Tolerance (506c, $200k) / 15-18% targets | **Deleted**; redirect → `/approach` |
| `/about` | "Unique Team and Strategy" + "Open to Joint Venture Opportunities" (mentions pocket deals, off shore resorts) | Replaced by new ABOUT |
| `/expertise` | Passive-investor pool description, 25/50-unit minimums, 506c $200k | **Deleted**; redirect → `/property-focus` |
| `/contact` | Form: First/Last, Phone, Email, Company, Address, City/State/Zip, "Are you an accredited investor? Yes/No" | Replaced by new CONTACT (no accreditation question) |
| `/disclosures` (footer link) | Long General Disclaimer + Financial Disclaimer with `[Sponsor Name]` / `[Scot Kenney]` placeholders | **Deleted**; redirect → `/website-notice` |
| "Investor Sign in" links (every page) | Portal link | **Deleted** |

Contact details confirmed from the live site: `Scot@scotkenneyacquisitions.com`, `530-415-0778`. No analytics tag was visible in the rendered pages (unverified — the raw source could not be fetched because the host blocks non-browser requests; confirm in Bluehost before cut-over).

## Change log

- 2026-10-11 — Repo created, staging enabled, spec locked, old site inventoried.
- 2026-10-11 — Full build pushed: HOME, APPROACH, PROPERTY FOCUS, ABOUT, CONTACT, WEBSITE NOTICE, 404; legacy `/invest` `/expertise` `/disclosures` redirect pages; `.nojekyll`. Verified on the live staging URL with headless Chromium: 0 console errors, all images load, banned-term scan clean, 1366px desktop + 390px mobile.
- 2026-10-11 — Fix: mobile menu had no background (header backdrop-filter made it the containing block for the fixed nav; explicit top/height now). CSS cache-buster v2.
- 2026-10-11 (afternoon) — Dante approved downloads. Owner images placed: `images/concept-motorcoach-resort.jpg` (phone photo of the architect's sketch, cropped to the paper, 1253x929) and `images/concept-community-entrance.jpg` (owner rendering, 1600x900, JPG from the 3 MB PNG). Contact form now posts to FormSubmit (`https://formsubmit.co/ajax/Scot@scotkenneyacquisitions.com`, no account; Scot must click the one-time activation email after the first submission). Honeypot renamed `_honey`, `_captcha=false`, table template. CSS v3 / JS v2.
- Copy-fidelity check vs the Word brief (`_source/brief.txt`, local only): 56 approved paragraphs, all present verbatim (2 flagged lines were button labels / the JS confirmation sentence).
- Pending: owner review + revisions; DNS cut-over.

## Items requiring owner (Scot) approval before publication

1. Review every page's copy (it is the brief's copy; confirm nothing drifted).
2. Confirm the two concept images and their captions on PROPERTY FOCUS.
3. Confirm the contact form destination address (`Scot@scotkenneyacquisitions.com`) and that the form relay account is in his name.
4. Confirm whether an analytics tag existed on the old site and should be carried over.
5. Approve desktop + mobile screenshots.
6. Then: DNS cut-over on Bluehost (A records → GitHub Pages, `www` CNAME). MX / email records are not touched.
