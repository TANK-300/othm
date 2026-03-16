with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Remove any previous broken injections
js = re.sub(r"html = html\.replace\('</head>', `<script>window\.CURRENT_REFERENCE.*?</script>\n</head>`\);\n", "", js, flags=re.DOTALL)

# Add it back correctly exactly once
injection = """
                let pdfUrl = '/viewer/view/view.pdf';
                if (record.pdfPath) {
                    pdfUrl = '/uploads/' + record.pdfPath;
                }
                
                // Inject both the reference and the exact PDF URL into the parent window
                html = html.replace('</head>', `<script>window.CURRENT_REFERENCE = '${record.reference}'; window.DIRECT_PDF_URL = '${pdfUrl}';</script>\n</head>`);
"""

# Place it right before the // 3. Replace any remaining visible DOM text
js = js.replace('// 3. Replace any remaining visible DOM text', injection.strip() + '\n\n                // 3. Replace any remaining visible DOM text')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
