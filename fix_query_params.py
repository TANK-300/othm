with open('verification.othm.org.uk/js/documentViewer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the concatenation logic so it's always valid query parameters!
import urllib.parse
js = js.replace(
    'dataPath += (window.CURRENT_REFERENCE ? "?ref=" + window.CURRENT_REFERENCE : "") + (window.DIRECT_PDF_URL ? "&pdf=" + encodeURIComponent(window.DIRECT_PDF_URL) : "");',
    'dataPath += "?ref=" + (window.CURRENT_REFERENCE || "") + "&pdf=" + encodeURIComponent(window.DIRECT_PDF_URL || "");'
)

with open('verification.othm.org.uk/js/documentViewer.js', 'w', encoding='utf-8') as f:
    f.write(js)
