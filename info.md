b
+256 753 155556
+256 773 555556

Buwate, Buwaate, Wakiso, Uganda

KIRA - KANSANGATI ROAD NEXT TO TOTAL, BUWATE, KAMPALA, UGANDA

https://www.facebook.com/DTurAds




git@github.com:hamzoooz/turads.com.git


after added user and get files and install requerments



sudo nano /etc/nginx/sites-enabled/django

upstream app_server {
    server unix:/home/django/gunicorn.socket fail_timeout=0;
}

server {
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    client_max_body_size 4G;
    server_name _;

    keepalive_timeout 5;

    # Your Django project's media files - amend as required
    location /media  {
        alias /home/django/django_project/django_project/media;
    }

    # your Django project's static files - amend as required
    location /static {
        alias /home/django/django_project/django_project/static;
    }

    # Proxy the static assests for the Django Admin panel
    location /static/admin {
       alias /usr/lib/python3/dist-packages/django/contrib/admin/static/admin/;
    }

    location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
            proxy_buffering off;

            proxy_pass http://app_server;
    }

}






server {
listen 80;
server_name turads.com www.turads.com ;
location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
autoindex on;
alias /home/django/turads/turads.com/staticfiles/;
}
location /media/ {
alias /home/django/turads/turads.com/media/;
}
location / {
include proxy_params;
proxy_pass http://unix:/home/django/turads/turads.com/core/app.sock;
}
    # Proxy the static assests for the Django Admin panel
    location /static/admin {
       alias /usr/lib/python3/dist-packages/django/contrib/admin/static/admin/;
    }

}

sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=Gunicorn daemon for Django Project
Before=nginx.service
After=network.target

[Service]
WorkingDirectory=/home/django/turads/turads.com
ExecStart=/usr/bin/gunicorn3 --name=turads --pythonpath=/home/django/turads/turads.com --bind unix:/home/django/gunicorn.socket --config /etc/gunicorn.d/gunicorn.py core.wsgi:application
Restart=always
SyslogIdentifier=gunicorn
User=django
Group=django

[Install]
WantedBy=multi-user.target



#apply change 
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo systemctl status gunicorn

PID=$(systemctl show --value -p MainPID gunicorn.service) && kill -HUP $PID

to get password and defualt user info

cat /root/.digitalocean_passwords



DJANGO_USER=django
DJANGO_USER_PASSWORD=9d8ffecbeeecf4e192dae0b778e686a6
DJANGO_POSTGRESS_PASS=4def3f69a37df221451736b39aa54cb6
DJANGO_SECRET_KEY=480df4052616d9b3407528d07e968f39
SECRET_KEY=bce6e01e02fc09420646b7532a204881
SETTINGS_FILE=/home/django/django_project/django_project/settings.py


[Unit]
Description=Gunicorn daemon for Django Project
After=network.target

[Service]
WorkingDirectory=/home/hamzoooz/turads/turads.com
ExecStart=/home/hamzoooz/turads/env/bin/gunicorn --workers=3 --name=turads.com --bind unix:/home/hamzoooz/gunicorn.socket core.wsgi:application
Restart=always
SyslogIdentifier=gunicorn
User=django
Group=django

[Install]
WantedBy=multi-user.target