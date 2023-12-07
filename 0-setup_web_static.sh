#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get -y install nginx

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

sed -i '/server_name _;/a \\n        location \/hbnb_static { \n            alias \/data\/web_static\/current;\n            index index.html index.htm;\n          }\n' /etc/nginx/sites-available/default

sudo service nginx restart
