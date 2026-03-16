with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Use regex to find and replace the script tag injection
js = re.sub(
    r'<script>window\.CURRENT_REFERENCE = \$\{record\.reference\}; window\.DIRECT_PDF_URL = \$\{pdfUrl\};</script>',
    '<script>window.CURRENT_REFERENCE = "${record.reference}"; window.DIRECT_PDF_URL = "${pdfUrl}";</script>',
    js
)

# And if I had quotes around them but not printed properly, let's just make absolutely sure
js = js.replace('<script>window.CURRENT_REFERENCE = ${record.reference}; window.DIRECT_PDF_URL = ${pdfUrl};</script>', '<script>window.CURRENT_REFERENCE = "${record.reference}"; window.DIRECT_PDF_URL = "${pdfUrl}";</script>')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
