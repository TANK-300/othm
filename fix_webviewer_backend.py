with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# We MUST FORCE WebViewer to use the FULL PDFTron backend (which has no domain license lock, only watermarks) instead of the 'pdf' backend (which IS PDF.js Express and has a hardcoded domain lock).
# The flag is `backendType: 'ems'` or `preloadWorker: 'pdf'`.
# Actually, the best way to ensure it uses PDFTron's full unlocked engine is `fullAPI: true` or `backendType: 'ems'`.

html = html.replace("extension: 'pdf',", "extension: 'pdf',\n            backendType: 'ems',\n            disableWebsockets: true,")

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
