import re

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change the endpoint from /viewer/view/view.pdf to /api/document/download
js = js.replace("app.get('/viewer/view/view.pdf'", "app.get('/api/document/download'")

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)


with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the iframe JS to request from the new endpoint
html = html.replace("let pdfUrl = '/viewer/view/view.pdf';", "let pdfUrl = '/api/document/download';")

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
