with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

pages_routes = """
// Route for footer pages
app.get('/Pages/:page', (req, res, next) => {
    const pageName = req.params.page;
    const validPages = ['Privacy', 'Faq', 'Terms', 'Support'];
    
    if (validPages.includes(pageName)) {
        res.sendFile(path.join(__dirname, 'verification.othm.org.uk', 'Pages', pageName + '.html'));
    } else {
        next();
    }
});
"""

if "app.get('/Pages/:page'" not in js:
    js = js.replace('// Serve all other static files', pages_routes + '\n// Serve all other static files')
    with open('server.js', 'w', encoding='utf-8') as f:
        f.write(js)
