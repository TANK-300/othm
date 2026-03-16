import re

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Change the multer configuration to preserve the original .pdf extension
# so that we CAN just load the URL directly.
multer_ext_fix = """
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
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));
"""

js = re.sub(r"const upload = multer\(\{ dest: uploadDir \}\);", multer_ext_fix, js)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)

