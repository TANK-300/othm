with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'html = html\.replace\(.*?\);', js)
for m in matches:
    print(m)
