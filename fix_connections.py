import re
import os

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Modify the connection URL replacement to point to relative /connections
js = js.replace('`https://dcwverify.othm.org.uk/connections?reference=${record.reference}`', '`/connections?reference=${record.reference}`')

# 2. Add the /connections route handler before the admin route
connections_code = """
// Serve static assets for the connections page (only paths that don't conflict with main site)
app.use('/assets/css', express.static(path.join(__dirname, 'dcwverify.othm.org.uk', 'assets', 'css')));
app.use('/assets/js', express.static(path.join(__dirname, 'dcwverify.othm.org.uk', 'assets', 'js')));

// Route for the 'Connect me' button (dcwverify site)
app.get('/connections', (req, res, next) => {
    const reference = req.query.reference;
    let htmlPath = path.join(__dirname, 'dcwverify.othm.org.uk', 'index.html');
    
    fs.readFile(htmlPath, 'utf8', (err, html) => {
        if (err) return next(err);

        if (reference) {
            const db = getDatabase();
            const record = db[reference];

            if (record) {
                // Replace name in connection page
                html = html.replace(/SHUAI BI/g, record.name);
                // Replace reference in connection page
                html = html.replace(/93998164-01-TNU8/g, record.reference);
                
                // Format date for connection page (DD/MM/YYYY)
                const d = new Date(record.dateOfAward);
                const day = String(d.getDate()).padStart(2, '0');
                const month = String(d.getMonth() + 1).padStart(2, '0');
                const year = d.getFullYear();
                const displayDate = `${day}/${month}/${year}`;
                
                html = html.replace(/21\\/12\\/2023/g, displayDate);
            }
        }
        res.send(html);
    });
});
"""

js = js.replace('// Admin panel route', connections_code + '\n// Admin panel route')

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
