#!/usr/bin/env bash
# http_header modified using puppet
exec { 'http_header':
       command => 'sudo apt-get -y update;
       sudo apt-get -y install nginx;
       sudo sed -i "/server_name _/a location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; }" /etc/nginx/sites-available/default;
       sudo service nginx restart',
       provider => shell
}