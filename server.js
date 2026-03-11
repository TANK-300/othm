const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const dbPath = path.join(__dirname, 'database.json');

// Initialize DB if not exists
if (!fs.existsSync(dbPath)) {
    fs.writeFileSync(dbPath, JSON.stringify({}));
}

function getDatabase() {
    const data = fs.readFileSync(dbPath, 'utf-8');
    return JSON.parse(data);
}

function saveDatabase(data) {
    fs.writeFileSync(dbPath, JSON.stringify(data, null, 2));
}

// API to create a new record
app.post('/api/save', (req, res) => {
    const data = req.body;
    if (!data.reference) {
        return res.status(400).json({ error: 'Reference is required' });
    }

    const db = getDatabase();
    db[data.reference] = {
        name: data.name,
        dateOfAward: data.dateOfAward,
        qualificationTitle: data.qualificationTitle,
        issuingBody: data.issuingBody || 'OTHM',
        reference: data.reference,
        uuid: '10c0f21d-696e-4243-5a73-08dbfa75cdb4' // we can just keep the static UUID for the PDF viewer
    };
    saveDatabase(db);
    res.json({ success: true, message: 'Saved successfully', record: db[data.reference] });
});

// Intercept requests for the main index.html to inject dynamic data
app.get(['/', '/index.html'], (req, res, next) => {
    const reference = req.query.reference;
    let htmlPath = path.join(__dirname, 'verification.othm.org.uk', 'index.html');
    
    // Read the static HTML
    fs.readFile(htmlPath, 'utf8', (err, html) => {
        if (err) return next(err);

        // If a reference is provided and we have it in our DB
        if (reference) {
            const db = getDatabase();
            const record = db[reference];

            if (record) {
                
                // 1. Replace the JSON data FIRST
                const verifyData = {
                    id: record.uuid,
                    fields: {
                        "Student Full Name": record.name,
                        "Issuing Body": record.issuingBody,
                        "Date of Award": record.dateOfAward,
                        "Qualification Title": record.qualificationTitle
                    },
                    metaData: {}
                };
                
                const hardcodedJson = /\{"id":"10c0f21d-696e-4243-5a73-08dbfa75cdb4","fields":\{"Student Full Name":"SHUAI BI","Issuing Body":"OTHM","Date of Award":"2023-12-21","Qualification Title":"OTHM Level 7 Diploma in Strategic Management and Leadership"\},"metaData":\{\}\}/g;
                html = html.replace(hardcodedJson, JSON.stringify(verifyData));

                // 2. Replace the data attributes
                html = html.replace(/data-reference="93998164-01-TNU8"/g, `data-reference="${record.reference}"`);
                html = html.replace(/https:\/\/dcwverify\.othm\.org\.uk\/connections\?reference=93998164-01-TNU8/g, `https://dcwverify.othm.org.uk/connections?reference=${record.reference}`);
                html = html.replace(/data-studentfullname="SHUAI BI"/g, `data-studentfullname="${record.name}"`);
                
                const formattedDate = `${record.dateOfAward}T00:00:00`;
                html = html.replace(/data-awarddate="2023-12-21T00:00:00"/g, `data-awarddate="${formattedDate}"`);

                // 3. Replace any remaining visible DOM text
                html = html.replace(/SHUAI BI/g, record.name);
                html = html.replace(/93998164-01-TNU8/g, record.reference);
                
                const d = new Date(record.dateOfAward);
                const day = String(d.getDate()).padStart(2, '0');
                const month = String(d.getMonth() + 1).padStart(2, '0');
                const year = d.getFullYear();
                const displayDate = day + "/" + month + "/" + year;
                
                html = html.replace(/21\/12\/2023/g, displayDate);

            }
        }
        res.send(html);
    });
});

// Admin panel route
app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'admin', 'index.html'));
});

// Serve all other static files for verification.othm.org.uk
app.use(express.static(path.join(__dirname, 'verification.othm.org.uk')));

const PORT = 8081;
app.listen(PORT, () => {
    console.log("Main Server running on http://localhost:8081");
    console.log("Admin Panel running on http://localhost:8081/admin");
});
