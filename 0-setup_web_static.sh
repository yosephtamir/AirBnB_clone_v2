#!/usr/bin/env bash
# Bash script that sets up a web server

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# make directories recursively
sudo mkdir -p /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared/

# echo message stored in index.html
echo "<h1>welcome to www.skydar.tech</h1>" > /data/web_static/releases/test/index.html

# prevent overwrite
if [ -d "/data/web_static/current" ];
then
	echo "path /data/web_static/current exists"
	sudo rm -rf /data/web_static/current;
# create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR $ubuntu:$ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
