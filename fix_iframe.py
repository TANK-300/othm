with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("pdfUrl += '?ref=' + ref;", "pdfUrl += '?ref=' + ref + '&fake=.pdf';")

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
