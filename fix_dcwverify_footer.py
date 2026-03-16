import shutil
import os

# Copy the pages to dcwverify so they work there too
os.makedirs('dcwverify.othm.org.uk/Pages', exist_ok=True)
for page in ['Privacy', 'Faq', 'Terms', 'Support']:
    shutil.copy(f'verification.othm.org.uk/Pages/{page}.html', f'dcwverify.othm.org.uk/Pages/{page}.html')

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add route for dcwverify pages as well, or we can just let express handle them if we add .html to the links
# But user wants exact URL `/Pages/Privacy` not `/Pages/Privacy.html`
dcw_pages = """
app.get('/Pages/:page', (req, res, next) => {
    // This route is already handled above for verification.othm.org.uk
    // Let's modify the above route to serve from dcwverify if host matches dcwverify.
    // Actually, both sites have identical footer pages, so serving from verification.othm.org.uk is perfectly fine!
    next();
});
"""
