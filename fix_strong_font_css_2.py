with open('verification.othm.org.uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see what the original element actually looks like in DevTools.
# `class="alert alert-success m-3 text-center" role="alert"`
# Inside is `<strong>This document is valid</strong> and was issued by <strong>OTHM</strong> to <strong>JOHN DOE</strong> on <strong>10/10/2024</strong>`
# Let's adjust the CSS to match Bootstrap 4's exact styling for strong tags if they are overridden, or increase the whole text size if the user means the whole alert text is too small!
# The user said "strong 字体小了". "Strong font is too small."
# BUT maybe my previous `fix_strong_font_css.py` injected it weirdly?
# Let's check how it got injected.
import re
print(re.search(r'<style>.*?alert-success strong.*?</style>', html, flags=re.DOTALL))
