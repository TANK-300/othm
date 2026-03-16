with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Since we stripped WebFont Loader, the browser defaulted to a totally different font-family (like Times New Roman or Arial) which renders MUCH larger and thicker!
# To restore the exact elegant original 13px Poppins look:
font_fix = """
    <!-- Fast Async Google Font to restore original 1:1 look -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Poppins', sans-serif !important; font-size: 13px !important; }
    </style>
</head>
"""

# Apply it
html = html.replace('</head>', font_fix)

with open('verification.othm.org.uk/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
