import re

with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Ensure uploads directory is explicitly created
multer_fix = """
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
}
const upload = multer({ dest: uploadDir });
"""

js = re.sub(r"const upload = multer\(\{ dest: 'uploads/' \}\);", multer_fix, js)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
