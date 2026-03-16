with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Change 13px to exactly 12px
html = html.replace('font-size: 13px !important;', 'font-size: 12px !important;')

with open('verification.othm.org.uk/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
