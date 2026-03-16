with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add Accessibility to the allowed routes
js = js.replace("const validPages = ['Privacy', 'Faq', 'Terms', 'Support'];", "const validPages = ['Privacy', 'Faq', 'Terms', 'Support', 'Accessibility'];")

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
