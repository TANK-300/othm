import re

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Revert the local /connections route usage to use the new exact domain provided by the user
# Find where we set the link
js = js.replace("`/connections?reference=${record.reference}`", "`https://dcwverify.verification.mom/connections?reference=${record.reference}`")

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
