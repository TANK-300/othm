with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add a middleware to support partial content / byte ranges since WebViewer requires it for PDF fetching
import re

range_support = """
// Add partial content support to all static files and specific endpoints
app.use((req, res, next) => {
    res.setHeader('Accept-Ranges', 'bytes');
    next();
});
"""

if "res.setHeader('Accept-Ranges', 'bytes');" not in js:
    js = js.replace('app.use(express.json());', range_support + '\napp.use(express.json());')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
