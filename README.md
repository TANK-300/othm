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

## 宝塔面板 (Baota/BT Panel) 部署教程

如果你使用的是宝塔面板，部署会更加简单，完全可视化操作：

1. **环境准备**：
   - 登录宝塔面板。
   - 在软件商店中搜索并安装 **PM2管理器** (或者 Node.js 版本管理器，安装 Node v16+)。
   - 在软件商店安装 **Nginx** (如果你还没安装的话)。

2. **上传代码**：
   - 点击左侧菜单的【文件】，进入 `/www/wwwroot/` 目录。
   - 点击【新建目录】，比如叫 `othm-verify`。
   - 进入这个目录，点击【终端】图标，运行 `git clone git@github.com:TANK-300/othm.git .` （或者你直接把本地的文件打包成 zip 在宝塔里上传解压）。

3. **启动 Node 项目**：
   - 打开宝塔的 **PM2管理器** 插件。
   - 确保 Node 版本在 16 以上。
   - 点击【添加项目】：
     - **项目所在目录**：选择你刚刚上传的目录 `/www/wwwroot/othm-verify`
     - **启动文件**：选择 `server.js`
     - **项目名称**：填 `othm-main`
     - 点击提交，主服务就跑起来了（端口 8081）。
   - 再次点击【添加项目】：
     - **启动文件**：选择 `server2.js`
     - **项目名称**：填 `othm-connections`
     - 点击提交，附属服务就跑起来了（端口 8082）。

4. **配置反向代理绑定域名（关键）**：
   - 点击宝塔左侧菜单的【网站】 -> 【添加站点】。
   - **域名**：填入你买好的主验证域名（例如：`verify.yourdomain.com`）。
   - **根目录**：随便选，因为我们不用它。
   - **PHP版本**：选“纯静态”。
   - 创建成功后，点击该网站右侧的【设置】 -> 左侧菜单找【反向代理】 -> 【添加反向代理】。
   - **代理名称**：随便填。
   - **目标URL**：填入 `http://127.0.0.1:8081`。
   - 提交保存。现在你就可以通过域名访问你的生成后台和验证页了！
   
   *(如果你想让跳转的 connections 页面也使用独立域名，就用同样的方法再建一个站点，比如 `connections.yourdomain.com`，反向代理的目标 URL 填 `http://127.0.0.1:8082` 即可)*
