with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Instead of blocking WebFont loader which takes forever in China, we can just use an async CSS link from Google Fonts or a fast CDN (like fontsource).
# The original font is "Poppins". We can add the CSS directly.
font_link = """
    <!-- Fast Async Google Font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Poppins', sans-serif; font-size: 13px !important; }
        .alert-success strong { font-size: inherit; }
    </style>
"""

# BUT WAIT, the user says "我看他的意思 整个 body 都是 12 px".
# Did the original CSS have `font-size: 12px;` somewhere?
# If `style.bundle.css` has `font-size: 1rem` which is 16px, where does the 12px or 13px come from?
# In `core.css` or `main.css`?
