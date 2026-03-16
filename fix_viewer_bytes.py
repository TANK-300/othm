with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Since WebViewer is complaining about byte ranges NOT being supported by the server, this implies NGINX might be stripping the 'Accept-Ranges' header, OR WebViewer is trying to fetch it but CORS fails, OR Nginx caches it poorly.
# The easiest fix is to tell WebViewer to NOT USE streaming/byte ranges and just download the whole file!
# There is a flag for WebViewer: `useDownloader: false` or `streaming: false`.
# Actually, the error says: "Could not use incremental download... Reason: Byte ranges are not supported by the server."
# But WebViewer should automatically fall back to downloading the full document! It's just a warning.
# Wait! Look at the VERY FIRST ERROR in the user's log:
# PDFJSDocumentType.js:118 A license key is required to use the view only build of PDF.js Express.

# WAIT.
# The user's log says:
# "PDFJSDocumentType.js:118 A license key is required to use the view only build of PDF.js Express. Get your free license key at https://pdfjs.express/profile (account required)"
#
# BUT I REPLACED PDF.JS EXPRESS WITH @pdftron/webviewer !!!!
# How can it STILL say "PDF.js Express" ???
# The user's server MUST BE running stale HTML, or the user's browser is caching the old `webviewer-core.min.js` which belongs to PDF.js Express!
