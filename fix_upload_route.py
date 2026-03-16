with open('server.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("app.use('/uploads', express.static(path.join(__dirname, 'uploads')));", "app.use('/uploads', express.static('/www/wwwroot/othm-uploads'));")

with open('server.js', 'w', encoding='utf-8') as f:
    f.write(js)
