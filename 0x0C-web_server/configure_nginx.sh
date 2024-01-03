#!/usr/bin/env bash
# Bash script to configure Nginx on the web-01 server

# Update the default Nginx configuration to serve "Hello World!" on root request
echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        server_name _;

        location / {
            echo 'Hello World!';
        }
    }" > /etc/nginx/sites-enabled/default

# Restart Nginx without using systemctl
service nginx restart
