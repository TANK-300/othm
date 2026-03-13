# OTHM Dynamic Verification Site

This is a dynamic cloned verification site powered by Node.js. It features a mock backend with an admin generator panel and dynamic HTML injection.

## Prerequisites

To run this project on a server (e.g., Ubuntu/Debian, CentOS, or AlmaLinux), you only need:
- **Node.js** (v14 or higher recommended)
- **npm** (comes with Node.js)
- **PM2** (optional, but highly recommended for keeping the server running in the background)

## Deployment Guide (Ubuntu/Debian)

### 1. Install Node.js
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 2. Clone your repository
```bash
git clone git@github.com:TANK-300/othm.git
cd othm
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Install PM2 (Process Manager)
This ensures your server automatically restarts if it crashes or the server reboots.
```bash
sudo npm install -g pm2
```

### 5. Start the Services
The project consists of two servers: the main verification site (port 8081) and the connection/details site (port 8082).
```bash
pm2 start server.js --name "othm-main"
pm2 start server2.js --name "othm-connections"
```

### 6. Make PM2 start on boot (Optional)
```bash
pm2 startup
pm2 save
```

### 7. Reverse Proxy (Nginx) - Highly Recommended
By default, the apps run on ports `8081` and `8082`. To serve them on port `80` or `443` (HTTPS) using a normal domain name, you should configure Nginx.

Example Nginx config for the main site:
```nginx
server {
    listen 80;
    server_name verification.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Example Nginx config for the connection site:
```nginx
server {
    listen 80;
    server_name dcwverify.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8082;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## How to use
1. Go to `http://<your-server-ip>:8081/admin`
2. Generate your data to receive your custom QR/Link.
