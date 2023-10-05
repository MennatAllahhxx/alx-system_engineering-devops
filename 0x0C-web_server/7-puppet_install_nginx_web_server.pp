#!/usr/bin/env bash
# install nginx using puppet
exec { 'nginx install':
       command => 'sudo apt-get -y update;
       sudo apt-get -y install nginx;
       sudo ufw allow 'Nginx HTTP';
       sudo sh -c "echo \"Hello World!\" > /var/www/html/index.nginx-debian.html";
       sudo sed -i "rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default;
       sudo service nginx restart',
       provider => shell
}