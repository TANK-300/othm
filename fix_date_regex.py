import re

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the regex so it matches the whole ISO string including milliseconds
js = js.replace('/data-awarddate="2023-12-21T00:00:00"/g', '/data-awarddate="2023-12-21T00:00:00.0000000"/g')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
