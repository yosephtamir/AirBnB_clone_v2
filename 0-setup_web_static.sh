#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	
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
" >  /etc/nginx/sites-available/default

sudo service nginx restart
