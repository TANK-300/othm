with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# When we pass `/uploads/xxxxx.pdf` to initialDoc, is there ANY REASON why WebViewer would fail?
# Yes! `pdfUrl` could be `/uploads/undefined` if DIRECT_PDF_URL is undefined but truthy? No.
# If `ref=23343434` doesn't have a pdfPath because the user didn't upload a PDF, `record.pdfPath` is null.
# So pdfUrl remains `/viewer/view/view.pdf`.
# Let's check `server.js` logic for `pdfUrl`!
