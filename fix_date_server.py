with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Fix all date parsing logic
date_fix = """
                const dateParts = record.dateOfAward.split('-'); // YYYY-MM-DD
                const year = dateParts[0];
                const month = dateParts[1];
                const day = dateParts[2];
                const displayDate = day + "/" + month + "/" + year;
"""

js = re.sub(
    r'const d = new Date\(record\.dateOfAward\);[\s\S]*?const displayDate = day \+ "/" \+ month \+ "/" \+ year;',
    date_fix.strip(),
    js
)

# And fix `server2.js` as well!
with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('server2.js', 'r', encoding='utf-8') as f:
    js2 = f.read()

js2 = re.sub(
    r'const d = new Date\(record\.dateOfAward\);[\s\S]*?const displayDate = `\$\{day\}/\$\{month\}/\$\{year\}`;',
    date_fix.strip(),
    js2
)

with open('server2.js', 'w', encoding='utf-8') as f:
    f.write(js2)
