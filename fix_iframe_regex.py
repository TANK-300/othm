with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

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

start = html.find('<script type="text/javascript">')
end = html.find('</script>', start) + 9
html = html[:start] + iframe_fix.strip() + html[end:]

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
