const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const multer = require('multer');

const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
}

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, uploadDir)
    },
    filename: function (req, file, cb) {
        cb(null, file.fieldname + '-' + Date.now() + '.pdf')
    }
});
const upload = multer({ storage: storage });

// Expose the uploads directory via static serving so we can just access URLs directly!





const app = express();
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));
app.use(express.urlencoded({ extended: true }));

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
app.post('/api/save', upload.single('pdfFile'), (req, res) => {
    const data = req.body || {};
    const file = req.file;
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
        uuid: '10c0f21d-696e-4243-5a73-08dbfa75cdb4',
        pdfPath: file ? file.filename : null
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
                html = html.replace(/https:\/\/dcwverify\.othm\.org\.uk\/connections\?reference=93998164-01-TNU8/g, `https://dcwverify.verification.mom/connections?reference=${record.reference}`);
                html = html.replace(/data-studentfullname="SHUAI BI"/g, `data-studentfullname="${record.name}"`);
                
                const formattedDate = `${record.dateOfAward}T00:00:00`;
                html = html.replace(/data-awarddate="2023-12-21T00:00:00"/g, `data-awarddate="${formattedDate}"`);
                
                // Pass the reference down into the viewer iframe
                html = html.replace(/viewer\/data\/false\/0\//g, 'viewer/data/false/0/'); // keep api mock static
                
                let dynamicPdfUrl = '/viewer/view/view.pdf';
                if (record.pdfPath) {
                    dynamicPdfUrl = '/uploads/' + record.pdfPath;
                }
                
                // Inject both the reference and the exact PDF URL into the parent window
                html = html.replace('</head>', `<script>window.CURRENT_REFERENCE = "${record.reference}"; window.DIRECT_PDF_URL = "${dynamicPdfUrl}";</script>\n</head>`);

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


// Serve the dynamic PDF based on the reference passed in query string
app.get('/api/document/download', (req, res, next) => {
    const reference = req.query.ref;
    if (reference) {
        const db = getDatabase();
        const record = db[reference];
        if (record && record.pdfPath) {
            const pdfFile = path.join(__dirname, 'uploads', record.pdfPath);
            if (fs.existsSync(pdfFile)) {
                res.set("Content-Type", "application/pdf");
                res.set("Content-Type", "application/pdf");
                return res.sendFile(pdfFile);
            }
        }
    }
    // Fallback to the default view.pdf
    res.set("Content-Type", "application/pdf");
    res.sendFile(path.join(__dirname, 'verification.othm.org.uk', 'viewer', 'view', 'view.pdf'));
});

// Intercept the iframe HTML to pass the reference down to the initialDoc
app.get('/viewer/view/10c0f21d-696e-4243-5a73-08dbfa75cdb4.html', (req, res, next) => {
    const reference = req.query.ref;
    let htmlPath = path.join(__dirname, 'verification.othm.org.uk', 'viewer', 'view', '10c0f21d-696e-4243-5a73-08dbfa75cdb4.html');
    
    fs.readFile(htmlPath, 'utf8', (err, html) => {
        if (err) return next(err);
        if (reference) {
            html = html.replace("initialDoc: '/viewer/view/view.pdf'", `initialDoc: '/viewer/view/view.pdf?ref=${reference}'`);
            html = html.replace("initialDoc: 'http://localhost:8081/viewer/view/view.pdf'", `initialDoc: 'http://localhost:8081/viewer/view/view.pdf?ref=${reference}'`);
        }
        res.send(html);
    });
});


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
