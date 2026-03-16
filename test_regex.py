import re
with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("Checking dcwverify domain replace:")
print('https://dcwverify.verification.mom' in js)

match = re.search(r'html = html\.replace\(/https:\\/\\/dcwverify\.othm\.org\.uk\\/connections\?reference=93998164-01-TNU8/g, `https://dcwverify\.verification\.mom/connections\?reference=\$\{record\.reference\}`\);', js)
print("Regex match:", match is not None)
if not match:
    # Print the line that has dcwverify.verification.mom
    for line in js.split('\n'):
        if 'dcwverify.verification.mom' in line:
            print(repr(line))
