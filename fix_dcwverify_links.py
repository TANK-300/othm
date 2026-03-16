import re

with open('dcwverify.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

matches = re.findall(r'.{0,20}93998164.{0,20}', html2)
for m in matches:
    print(m)
