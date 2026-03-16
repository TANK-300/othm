with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add Cache-Control headers to the intercepting routes to ensure browsers never cache the replaced HTML
headers = """
        res.set('Cache-Control', 'no-store, no-cache, must-revalidate, private');
        res.set('Expires', '-1');
        res.set('Pragma', 'no-cache');
        res.send(html);
"""

js = js.replace('res.send(html);', headers)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
