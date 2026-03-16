with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Change the uploadDir from 'path.join(__dirname, "uploads")' to '/www/wwwroot/othm-uploads'
upload_dir_setup = """
const uploadDir = '/www/wwwroot/othm-uploads';
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
}
"""

js = re.sub(r'const uploadDir = path\.join\(__dirname, \'uploads\'\);\nif \(!fs\.existsSync\(uploadDir\)\) \{\n    fs\.mkdirSync\(uploadDir, \{ recursive: true \}\);\n\}', upload_dir_setup.strip(), js)

# Change the database path to be outside the project dir too so data isn't lost
db_setup = """
const dataDir = '/www/wwwroot/othm-data';
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}
const dbPath = path.join(dataDir, 'database.json');
"""
js = re.sub(r"const dbPath = path\.join\(__dirname, 'database\.json'\);", db_setup.strip(), js)

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('server2.js', 'r', encoding='utf-8') as f:
    js2 = f.read()

js2 = re.sub(r"const dbPath = path\.join\(__dirname, 'database\.json'\);", db_setup.strip(), js2)

with open('server2.js', 'w', encoding='utf-8') as f:
    f.write(js2)

