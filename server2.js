const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app2 = express();
app2.use(cors());


const dbPath = path.join(__dirname, 'database.json');

function getDatabase() {
    if (fs.existsSync(dbPath)) {
        return JSON.parse(fs.readFileSync(dbPath, 'utf-8'));
    }
    return {};
}

app2.get(['/connections', '/index.html', '/'], (req, res, next) => {
    const reference = req.query.reference;
    let htmlPath = path.join(__dirname, 'dcwverify.othm.org.uk', 'index.html');
    
    fs.readFile(htmlPath, 'utf8', (err, html) => {
        if (err) return next(err);

        if (reference) {
            const db = getDatabase();
            const record = db[reference];

            if (record) {
                console.log("Server 2 got reference:", reference, record);
                // Replace name in connection page
                html = html.replace(/SHUAI BI/g, record.name);
                // Replace reference in connection page
                html = html.replace(/93998164-01-TNU8/g, record.reference);
                
                // Format date for connection page (DD/MM/YYYY)
                const dateParts = record.dateOfAward.split('-'); // YYYY-MM-DD
                const year = dateParts[0];
                const month = dateParts[1];
                const day = dateParts[2];
                const displayDate = day + "/" + month + "/" + year;
                
                html = html.replace(/21\/12\/2023/g, displayDate);
            }
        }
        res.send(html);
    });
});


// Route for footer pages
app2.get('/Pages/:page', (req, res, next) => {
    const pageName = req.params.page;
    const validPages = ['Privacy', 'Faq', 'Terms', 'Support'];
    
    if (validPages.includes(pageName)) {
        res.sendFile(path.join(__dirname, 'dcwverify.othm.org.uk', 'Pages', pageName + '.html'));
    } else {
        next();
    }
});

// Serve dcwverify static files
app2.use(express.static(path.join(__dirname, 'dcwverify.othm.org.uk')));

const PORT2 = 8082;
app2.listen(PORT2, () => {
    console.log(`Connection Server running on http://localhost:${PORT2}`);
});
