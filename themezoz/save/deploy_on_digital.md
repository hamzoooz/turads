after added user and get files and install requerments

sudo nano /etc/nginx/sites-enabled/django

server {
listen 80;
server_name book-hope.com www.book-hope.com ;
location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
autoindex on;
alias /home/django/sbaq/staticfiles/;
}
location /media/ {
alias /home/django/sbaq/media/;
}
location / {
include proxy_params;
proxy_pass http://unix:/home/django/sbaq/sbaq_design/app.sock;
}
}

sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=Gunicorn daemon for Django Project
Before=nginx.service
After=network.target

[Service]
WorkingDirectory=/home/django/sbaq
ExecStart=/usr/bin/gunicorn3 --name=sbaq --pythonpath=/home/django/sbaq --bind unix:/home/django/gunicorn.socket --config /etc/gunicorn.d/gunicorn.py sbaq_design.wsgi:application
Restart=always
SyslogIdentifier=gunicorn
User=django
Group=django

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo systemctl status gunicorn

PID=$(systemctl show --value -p MainPID gunicorn.service) && kill -HUP $PID

to get password and defualt user info

cat /root/.digitalocean_passwords
