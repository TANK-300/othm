with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the specific URL format
js = js.replace('https://dcwverify.othm.org.uk/connections?reference=${record.reference}', '/connections?reference=${record.reference}')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
