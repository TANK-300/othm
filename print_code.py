import re
with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

match = re.search(r'let pdfUrl.*?</head>`\);', js, flags=re.DOTALL)
if match:
    print("MATCH 1:")
    print(repr(match.group(0)))

# Let's see if there are MULTIPLE replacements
matches = re.findall(r'html = html\.replace.*CURRENT_REFERENCE.*?;', js, flags=re.DOTALL)
print(f"Found {len(matches)} replacements")
for m in matches:
    print(repr(m))
