with open('verification.othm.org.uk/js/documentViewer.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change documentViewer.js to pass BOTH ref and pdf URL to the iframe
import re
js = js.replace('dataPath += (window.CURRENT_REFERENCE ? "?ref=" + window.CURRENT_REFERENCE : "");', 
                'dataPath += (window.CURRENT_REFERENCE ? "?ref=" + window.CURRENT_REFERENCE : "") + (window.DIRECT_PDF_URL ? "&pdf=" + encodeURIComponent(window.DIRECT_PDF_URL) : "");')

with open('verification.othm.org.uk/js/documentViewer.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Have the iframe read the 'pdf' query parameter instead of window.parent
iframe_fix = """
    <script type="text/javascript">
        const urlParams = new URLSearchParams(window.location.search);
        const ref = urlParams.get('ref');
        const pdfQuery = urlParams.get('pdf');
        
        let pdfUrl = '/viewer/view/view.pdf';
        
        if (pdfQuery) {
            pdfUrl = pdfQuery;
        } else {
            try {
                if (window.parent && window.parent.DIRECT_PDF_URL) {
                    pdfUrl = window.parent.DIRECT_PDF_URL;
                }
            } catch(e) {}
        }

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

html = re.sub(r'<script type="text/javascript">\n        // Read the exact direct URL injected by the server.*?});\n    </script>', iframe_fix.strip(), html, flags=re.DOTALL)

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
