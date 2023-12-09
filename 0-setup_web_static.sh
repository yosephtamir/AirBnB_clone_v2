#!/usr/bin/env bash
# used to download and setup nginx
apt update
apt install -y nginx
echo "Holberton School for the win! " > /var/www/html/index.html

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Holberton School" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By 3743-web-01;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;

        location / {
            root /etc/nginx/html;
            index index.html index.htm;
        }

        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
        error_page 404 /404.html;
        location /404 {
            root /etc/nginx/html;
            internal;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

}
" > /etc/nginx/sites-available/default
systemctl restart nginx
