import urllib.request
print("If backendType: 'ems' fails, another way to bypass PDFJS express is to use the `disableStreaming: true` flag to avoid the byte ranges error that the user ALSO got.")

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a backup parameter just in case
html = html.replace("disableWebsockets: true,", "disableWebsockets: true,\n            streaming: false,")

with open('verification.othm.org.uk/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', 'w', encoding='utf-8') as f:
    f.write(html)
