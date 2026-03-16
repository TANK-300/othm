with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a CSS rule to index.html to make the `strong` tag inside the alert box bigger.
# The alert box is `<div class="alert alert-success m-3 text-center" role="alert">...</div>`
css_fix = """
    <style>
        .alert-success strong {
            font-size: 1.1em; /* Make it slightly larger */
            font-weight: 700; /* Bolder */
        }
    </style>
</head>
"""

html = html.replace('</head>', css_fix)

with open('verification.othm.org.uk/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
