with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# The user wants these links to point to the actual official website https://verification.othm.org.uk
html = html.replace('href="/Pages/Privacy"', 'target="_blank" href="https://verification.othm.org.uk/Pages/Privacy"')
html = html.replace('href="/Pages/Faq"', 'target="_blank" href="https://verification.othm.org.uk/Pages/Faq"')
html = html.replace('href="/Pages/Terms"', 'target="_blank" href="https://verification.othm.org.uk/Pages/Terms"')
html = html.replace('href="/Pages/Support"', 'target="_blank" href="https://verification.othm.org.uk/Pages/Support"')

with open('verification.othm.org.uk/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
