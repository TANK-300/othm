with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Clean up ALL duplicate injections
# Find the start and end of the injection block
start_str = "html = html.replace(/data-awarddate"
end_str = "html = html.replace(/SHUAI BI"
start_idx = js.find(start_str)
end_idx = js.find(end_str)

clean_chunk = """html = html.replace(/data-awarddate="2023-12-21T00:00:00"/g, `data-awarddate="${formattedDate}"`);
                
                // Pass the reference down into the viewer iframe
                html = html.replace(/viewer\\/data\\/false\\/0\\//g, 'viewer/data/false/0/'); // keep api mock static
                
                let dynamicPdfUrl = '/viewer/view/view.pdf';
                if (record.pdfPath) {
                    dynamicPdfUrl = '/uploads/' + record.pdfPath;
                }
                
                // Inject both the reference and the exact PDF URL into the parent window
                html = html.replace('</head>', `<script>window.CURRENT_REFERENCE = "${record.reference}"; window.DIRECT_PDF_URL = "${dynamicPdfUrl}";</script>\\n</head>`);

                // 3. Replace any remaining visible DOM text
                """

js = js[:start_idx] + clean_chunk + js[end_idx:]

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
