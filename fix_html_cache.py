with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

html_cache_buster = """
                // Add meta anti-caching to the top of the HTML just in case headers are stripped by proxies
                html = html.replace('<head>', `<head>\\n<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\\n<meta http-equiv="Pragma" content="no-cache">\\n<meta http-equiv="Expires" content="0">`);
"""

# Ensure it's there
if "meta http-equiv" not in js:
    js = js.replace('// 1. Replace the JSON data FIRST', html_cache_buster + '\n                // 1. Replace the JSON data FIRST')
    with open('server.js', 'w', encoding='utf-8') as f:
        f.write(js)

