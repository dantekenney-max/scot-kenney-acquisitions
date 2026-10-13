# Domain cutover plan: scotkenneyacquisitions.com -> new site (GitHub Pages)

Checked 2026-10-13 with live DNS lookups (Google DNS 8.8.8.8 and ns1.hostmonster.com).

## Where it is today
| Record | Value | Notes |
|---|---|---|
| Nameservers | ns1/ns2.hostmonster.com | Bluehost family. DNS is edited in the Bluehost panel. |
| `@` A | 67.20.76.83 | Bluehost server running the old WordPress site |
| `www` | alias of `@` | |
| MX | `scotkenneyacquisitions.com` (pref 10) and `mail.scotkenneyacquisitions.com` (pref 0) | **Email depends on the `@` record** |
| `mail` A | 67.20.76.83 | |
| `webmail` | alias of `@` | **breaks if `@` moves** |
| SPF TXT | `v=spf1 a mx include:websitewelcome.com ~all` | `a` means "the `@` server", which is moving |

## The risk
If only the `@` record moves to GitHub, Scot's email (scot@scotkenneyacquisitions.com) partly breaks:
one MX record, webmail, and the SPF "a" rule all point at `@`.

## Safe order (all in Bluehost > Domains > scotkenneyacquisitions.com > DNS)
1. **Protect email first**
   - MX: delete the MX that points to `scotkenneyacquisitions.com`; keep `mail.scotkenneyacquisitions.com` (A 67.20.76.83).
   - `webmail`: change from alias of `@` to A record 67.20.76.83.
   - SPF TXT: `v=spf1 ip4:67.20.76.83 mx include:websitewelcome.com ~all`
   - Check any other CNAMEs aliased to `@` (cpanel, autodiscover, ftp) and repoint them to A 67.20.76.83.
   - Wait for these to publish (Bluehost quirk: if the panel looks right but lookups don't change, edit and re-save one record's TTL).
2. **Point the website**
   - `@`: replace A 67.20.76.83 with the four GitHub Pages A records 185.199.108.153 / .109.153 / .110.153 / .111.153
   - `www`: CNAME -> dantekenney-max.github.io
3. **GitHub side** (same pattern as blackfootlavenderretreat.com)
   - Add `CNAME` file containing `scotkenneyacquisitions.com` to the repo root. Do this at the same time as step 2, not before; it makes the preview link redirect to the domain.
   - Repo Settings > Pages > custom domain set, then tick "Enforce HTTPS" once the certificate is issued (minutes to a few hours).
4. **Verify**
   - Domain and www load the new site over https, all pages, no broken images.
   - Old WordPress URLs (/expertise, /invest, /disclosures, /terms) land on the redirect pages.
   - Send a test email to scot@scotkenneyacquisitions.com and confirm it arrives, and that webmail still opens.

## Rollback
Put `@` back to A 67.20.76.83 and remove the CNAME file. The old WordPress site is untouched on the Bluehost server the whole time.

## Gates before doing it
- Scot's explicit OK to go live (his own instructions say do not publish to the live domain without his approval).
- Someone logged into the Bluehost account that holds this domain (Claude cannot enter passwords).
