# 🔐 Nginx + acme.sh HTTPS 反代 Emby

## 1. 安装 acme.sh
```bash
curl https://get.acme.sh | sh
```

## 2. DNS API 签发证书（以 DNSPod 为例）
```bash
export DP_Id="123456"
export DP_Key="xxxxxxxxxxxxxxxxxxxx"
~/.acme.sh/acme.sh --issue --dns dns_dp -d emby.example.com
```

## 3. 安装证书
```bash
~/.acme.sh/acme.sh --install-cert -d emby.example.com \
--key-file /etc/nginx/ssl/emby.key \
--fullchain-file /etc/nginx/ssl/emby.crt \
--reloadcmd "systemctl reload nginx"
```

## 4. Nginx 配置（监听高位端口）
```nginx
server {
  listen 18443 ssl;
  server_name emby.example.com;

  ssl_certificate     /etc/nginx/ssl/emby.crt;
  ssl_certificate_key /etc/nginx/ssl/emby.key;

  location / {
    proxy_pass http://192.168.100.10:8096;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
  }
}
```
