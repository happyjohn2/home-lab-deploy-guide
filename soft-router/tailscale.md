# 🚀 iStoreOS 安装最新版 Tailscale 教程（非 opkg）

## 1. 卸载旧版 tailscale
```bash
opkg remove tailscale tailscaled luci-app-tailscale --force-removal-of-dependent-packages
rm -f /usr/sbin/tailscale /usr/sbin/tailscaled
rm -rf /var/lib/tailscale
```

## 2. 下载并部署新版
```bash
cd /root
wget https://pkgs.tailscale.com/stable/tailscale_1.82.5_amd64.tgz
tar -xzvf tailscale_1.82.5_amd64.tgz
cd tailscale_1.82.5_amd64
cp tailscale tailscaled /usr/sbin/
chmod +x /usr/sbin/tailscale /usr/sbin/tailscaled
```

## 3. 创建 `/etc/init.d/tailscaled` 自启脚本
```sh
#!/bin/sh /etc/rc.common
START=99
STOP=10

start() {
  /usr/sbin/tailscaled &
  sleep 3
  /usr/sbin/tailscale up --accept-routes --advertise-exit-node --advertise-routes=192.168.100.0/24
}

stop() {
  killall tailscaled
}
```
```bash
chmod +x /etc/init.d/tailscaled
/etc/init.d/tailscaled enable
/etc/init.d/tailscaled start
```
