with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Modify server.js to inject the direct URL of the PDF instead of an API route.
# Find the iframe injection logic and pass the actual PDF url

parent_injection = """
                // Pass the direct PDF URL to the iframe if it exists
                let pdfUrl = '/viewer/view/view.pdf';
                if (record.pdfPath) {
                    pdfUrl = '/uploads/' + record.pdfPath;
                }
                
                html = html.replace('</head>', `<script>window.CURRENT_REFERENCE = "${record.reference}"; window.DIRECT_PDF_URL = "${pdfUrl}";</script>\n</head>`);
"""
import re
js = re.sub(r"html = html\.replace\('</head>', `<script>window\.CURRENT_REFERENCE = \"\$\{record\.reference\}\";</script>\\n</head>`\);", parent_injection, js)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change the iframe to just read DIRECT_PDF_URL from the parent window
iframe_fix = """
    <script type="text/javascript">
        // Read the exact direct URL injected by the server into the parent window
        let pdfUrl = '/viewer/view/view.pdf';
        try {
            if (window.parent && window.parent.DIRECT_PDF_URL) {
                pdfUrl = window.parent.DIRECT_PDF_URL;
            }
        } catch(e) {}

        WebViewer({
            initialDoc: pdfUrl,
            path: '/lib/webviewer/public',
            extension: 'pdf',
        }, document.getElementById('viewer')).then(instance => {
            instance.UI.disableElements(['contextMenuPopup', 'selectToolButton', 'themeChangeButton', 'languageButton']);
            instance.UI.disableFeatures([instance.UI.Feature.Print, instance.UI.Feature.Download, instance.UI.Feature.PageNavigation, instance.UI.Feature.Search, instance.UI.Feature.TextSelection, instance.UI.Feature.Annotations]);
        });
    </script>
"""

html = re.sub(r'<script type="text/javascript">\n        const urlParams.*?</script>', iframe_fix.strip(), html, flags=re.DOTALL)

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
