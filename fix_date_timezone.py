with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# If the user selects 2024-10-10, `dateOfAward` is "2024-10-10".
# In server.js, we do `const formattedDate = \`${record.dateOfAward}T00:00:00\`;`
# Then we inject `data-awarddate="2024-10-10T00:00:00"`.
# In JS, `moment("2024-10-10T00:00:00")` will be parsed in local timezone.
# If the user's browser is behind UTC (like USA), it might show "10/09/2024".
# To fix this, we should inject the date string without the "T00:00:00" or add a timezone offset, or just use "12:00:00" noon to be safe from 1 day timezone shifts!
# `2024-10-10T12:00:00` guarantees it stays the same date anywhere on earth (mostly).

js = js.replace('const formattedDate = `${record.dateOfAward}T00:00:00`;', 'const formattedDate = `${record.dateOfAward}T12:00:00`;')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
