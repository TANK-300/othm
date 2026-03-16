with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change the hardcoded domain to the new one
js = js.replace('https://dcwverify.verification.mom/connections', 'https://dcwverify.quolificalions.com/connections')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
