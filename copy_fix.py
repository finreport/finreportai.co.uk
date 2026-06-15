import os

def r(content, old, new, require=True):
    if require and old not in content:
        raise AssertionError(f"NOT FOUND: {repr(old[:80])}")
    return content.replace(old, new)

# ─── INDEX.HTML ───────────────────────────────────────────────────────────────
path = '/home/user/finreportai.co.uk/index.html'
c = open(path).read()

# 1. Hero h1 (three hl-line spans)
c = r(c,
    '<span class="hl-line-wrap"><span class="hl-line" data-hero>Turn your Xero export</span></span>\n      <span class="hl-line-wrap"><span class="hl-line" data-hero>into a client report</span></span>\n      <span class="hl-line-wrap"><span class="hl-line" data-hero>in <strong class="grad">15 minutes.</strong></span></span>',
    '<span class="hl-line-wrap"><span class="hl-line" data-hero>Turn your Xero export into</span></span>\n      <span class="hl-line-wrap"><span class="hl-line" data-hero>a premium client report</span></span>\n      <span class="hl-line-wrap"><span class="hl-line" data-hero>in <strong class="grad">minutes.</strong></span></span>'
)

# 2. Hero sub paragraph
c = r(c,
    'Upload your client\'s P&amp;L from Xero, QuickBooks, Sage or Excel. Within 15 minutes you\'ll have a branded PDF — plain English summary, visual charts, a business health score, and colour-coded analyst flags — ready to forward. No design work. No formatting. No follow-up calls explaining what the numbers mean.',
    'Upload any raw P&amp;L from Xero, QuickBooks, Sage, or Excel. In under 2 minutes you\'ll have a beautifully branded PDF — plain English summary, visual charts, margin analysis, and UK tax and VAT flags — ready to send straight to your client.'
)

# 3. Meta description
c = r(c, 'in 15 minutes. Built for UK accountancy firms.', 'in under 2 minutes. Built for UK accountancy firms.')
# OG description
c = r(c, 'receive a client-ready report in 15 minutes.', 'receive a client-ready report in under 2 minutes.')
# Twitter description
c = r(c, 'receive a client-ready report in 15 minutes. From', 'receive a client-ready report in under 2 minutes. From', require=False)
# JSON-LD description
c = r(c, 'receive a professional, client-ready report in 15 minutes.', 'receive a professional, client-ready report in under 2 minutes.')

# 4. Marquee (appears twice)
c = c.replace('15 min delivery', '2 min delivery')

# 5. Stats strip — value, count attr, suffix text, description
c = r(c,
    '<div class="stat-num"><span data-count="15" data-suffix="min">15min</span></div>\n      <div class="stat-desc">Average time from upload to finished PDF in your inbox</div>',
    '<div class="stat-num"><span data-count="2" data-suffix="min">2min</span></div>\n      <div class="stat-desc">Minutes from CSV upload to PDF in your inbox</div>'
)

# 6. prob-fix link
c = r(c, 'FinReportAI fixes this in 15 minutes →', 'FinReportAI fixes this in under 2 minutes →')

# 7. How it works step 2
c = r(c, 'It takes under 15 minutes.', 'It takes under 2 minutes.')

# 8. How it works step 3 — "within 15 minutes"
c = r(c, 'arrives in your inbox within 15 minutes. Review it', 'arrives in your inbox in under 2 minutes. Review it')

# 9. Pricing feature list
c = r(c, 'PDF in your inbox within 15 minutes of upload', 'PDF in your inbox in under 2 minutes of upload')

# 10. FAQ answer for delivery time
c = r(c,
    '15 minutes on average. You receive a confirmation email the moment your file is uploaded, and the finished PDF arrives in your inbox shortly after. If it hasn\'t landed within 20 minutes, email reports@finreportai.co.uk and we\'ll prioritise it immediately.',
    'Typically under 2 minutes from uploading your data. You\'ll receive a confirmation and the finished PDF arrives in your inbox shortly after.'
)

# 11. Final CTA paragraph
c = r(c, 'receive a professional report in your inbox within 15 minutes.', 'receive a professional report in your inbox in under 2 minutes.')

# 12. Footer tag
c = r(c, 'delivered to your inbox in 15 minutes.', 'delivered to your inbox in under 2 minutes.')

open(path, 'w').write(c)
print('✓ index.html done')

# ─── SAMPLE.HTML ──────────────────────────────────────────────────────────────
path = '/home/user/finreportai.co.uk/sample.html'
c = open(path).read()

# Marquee (appears twice)
c = c.replace('Delivered in 15 minutes', 'Delivered in under 2 minutes')

# Mid-CTA "within 15 minutes"
c = r(c, 'receive a report like this one within 15 minutes.', 'receive a report like this one in under 2 minutes.')

# Footer tag
c = r(c, 'Powered by AI. Delivered in 15 minutes.', 'Powered by AI. Delivered in under 2 minutes.', require=False)
c = r(c, 'Delivered in 15 minutes.', 'Delivered in under 2 minutes.', require=False)

open(path, 'w').write(c)
print('✓ sample.html done')

# ─── 404.HTML ─────────────────────────────────────────────────────────────────
path = '/home/user/finreportai.co.uk/404.html'
c = open(path).read()

c = c.replace('Delivered in 15 minutes', 'Delivered in under 2 minutes')
c = c.replace('in 15 min', 'in under 2 min')

open(path, 'w').write(c)
print('✓ 404.html done')

# ─── STATUS.HTML ──────────────────────────────────────────────────────────────
path = '/home/user/finreportai.co.uk/status.html'
c = open(path).read()

c = r(c, 'within <strong style="color:var(--navy)">15 minutes</strong> of submission', 'within <strong style="color:var(--navy)">2 minutes</strong> of submission')
c = c.replace('Delivered in 15 minutes', 'Delivered in under 2 minutes')

open(path, 'w').write(c)
print('✓ status.html done')

# ─── TERMS.HTML ───────────────────────────────────────────────────────────────
path = '/home/user/finreportai.co.uk/terms.html'
c = open(path).read()

c = r(c,
    'typically within 15 minutes of submission. The 15-minute delivery time is a target, not a guarantee; actual delivery times may vary.',
    'typically within 2 minutes of submission. The 2-minute delivery time is a target, not a guarantee; actual delivery times may vary.'
)
c = c.replace('Delivered in 15 minutes', 'Delivered in under 2 minutes')

open(path, 'w').write(c)
print('✓ terms.html done')

print('\nAll done.')
