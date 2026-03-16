with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I found the BUG!
# Look at this line in server.js: `html = html.replace(/93998164-01-TNU8/g, record.reference);`
# Wait... if I inject `<script>window.CURRENT_REFERENCE = '93998164-01-TNU8';</script>` (if the original reference was that)
# Then it gets replaced. BUT the reference is 23343434!
# But look at THIS line: `html = html.replace(/'/g, ...)` ? No.

# Wait, `html = html.replace(/SHUAI BI/g, record.name);`
# What if `record.reference` is a number, not a string?
# `const data = req.body` -> `data.reference` could be a string.
# Why are the quotes missing??

# Look at the curl output: `<script>window.CURRENT_REFERENCE = 23343434; window.DIRECT_PDF_URL = /uploads/pdfFile-1773632371070.pdf;</script>`
# The quotes literally disappeared!
# Wait! Did I run `html = html.replace(/'/g, ...)` somewhere? NO.

# OH I SEE IT!
# Let me look at `fix_quotes.py` I ran earlier!
import re
print("Dumping server.js replacement block:")
match = re.search(r'let pdfUrl.*?</head>`\);', js, flags=re.DOTALL)
print(match.group(0))

