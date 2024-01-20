# after create instance or server 
# Step one 
sudo apt-get update & sudo apt-get upgrade -y 
sudo adduser hamzoooz 
sudo usermod -aG sudo hamzoooz
sudo visudo # to don't ask for passowrd always 
# in file add the folloing line
hamzoooz  ALL=(ALL) NOPASSWD:ALL

<!-- 143.198.130.243| -->
## create djanog on home
sudo mkdir themezoz
sudo chown hamzoooz:hamzoooz -R themezoz 
# To check the Check the woner for dir must be for new user  

# Step tow 
su - hamzoooz # login to your account 
install python3-venv python3-pip supervisor -y  # gunicorn 
sudo apt-get install python3-venv python3-pip supervisor -y  # gunicorn 
# create env and active and 
# and clone your project and install requerment filse 
python3 -m venv env 
source  env/bin/activate

git clone djanog 
git clone git@github.com:hamzoooz/themezoz.git
pip install -r requerment.txt 
sudo pip3 install gunicorn 
sudo apt-get install supervisor 
sudo apt-get install nginx 

pip install gunicorn 
## to check every thing it work good or no 
### you must be allow setup djanog and server to allow run in this port 


python manage.py runserver 0.0.0.0:8000

# Step Three Supervisor and gunicorn 
cd /etc/supervisor/conf.d/
sudo nano gunicorn.conf

~~~bach

[program:gunicorn]
directory=/home/ubuntu/themezoz
command=/home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/themezoz/app.sock themezoz.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log
[group:guni]
programs:gunicorn

~~~
sudo mkdir /var/log/gunicorn

# check it work ? 
sudo supervisorctl reread
>> guni: available
sudo supervisorctl update
>> guni: added process group
sudo supervisorctl status 

sudo nano /etc/nginx/nginx.conf


#Step Four NGINX 
sudo apt install nginx
cd /etc/nginx/sites-available/djanog.conf

 
server {
        listen 80;
        server_name themezoz.com www.themezoz.com 18.232.91.199 ;
        location / {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/themezoz/app.sock;
        }
        location /static/ {
                autoindex on;
                alias /home/ubuntu/themezoz/staticfile/;
        }
}

 
sudo ln djanog.conf  /etc/nginx/sites-enabled/

sudo service nginx restart
sudo nginx -t 

python manage.py  collectstatic
# Step Five in install Free SSL with certbot 
=======
```
sudo nginx -t
sudo service nginx restart

python manage.py collectstatic
 
sudo apt install certbot python3-certbot-nginx -y 
sudo certbot 

server {
    listen 80;
    server_name themezoz.com www.themezoz.com ;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/themezoz/themezoz/staticfile/;
    }
    location /media/ {
        root /home/themezoz/themezoz//media;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/themezoz/env/bin/gunicorn.sock;
    }
}


sudo ln -s /etc/nginx/sites-available/djanog.conf /etc/nginx/sites-enabled/





















<!-- for themezoz -->
ssh -i "themezoz.com.pem" ubuntu@ec2-54-175-227-249.compute-1.amazonaws.com


<!-- for shopyblack -->
ssh -i "themezoz.com.pem" ubuntu@ec2-54-159-9-249.compute-1.amazonaws.com
<!--  https://m.do.co/c/66872a7e0532 -->
 Hamzoooz@0784512346#themezoz.com

ssh -i save/hamzoooz.pem hamzoooz@20.224.165.69


# after create instance or server 
# Step one 
sudo apt-get update & sudo apt-get upgrade -y 
sudo adduser hamzoooz 
sudo usermod -aG sudo hamzoooz
sudo visudo # to don't ask for passowrd always 
# in file add the folloing line   
hamzoooz  ALL=(ALL) NOPASSWD:ALL   
 

sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql


CREATE DATABASE themezoz;
CREATE USER themezoz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';
ALTER ROLE themezoz SET client_encoding TO 'utf8';
ALTER ROLE themezoz SET default_transaction_isolation TO 'read committed';
ALTER ROLE themezoz SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE themezoz TO themezoz;
ALTER DATABASE themezoz  OWNER TO themezoz;
\q

sudo nano /etc/postgresql/<version>/main/postgresql.conf
listen_addresses = '*'
sudo systemctl restart postgresql

sudo nano /etc/postgresql/<version>/main/pg_hba.conf
host    replication     all             192.168.1.100/24        md5
host    replication     all             20.56.150.190/24        md5
host    themezoz        themezoz        0.0.0.0/8            md5

local   all   themezoz   md5


sudo -u postgres psql -d template1
\q

sudo systemctl start postgresql
sudo systemctl enable postgresql

<!-- python -c "import sqlparse; print(sqlparse.format(open('data_dump.sql').read(), reindent=True, keyword_case='upper'))" > postgresql_data_dump.sql
psql -U themezoz -d themezoz -f postgresql_data_dump.sql -->


## create djanog on home
sudo mkdir themezoz
sudo chown hamzoooz:hamzoooz -R themezoz 
# To check the Check the woner for dir must be for new user  


# Step tow 
su - hamzoooz # login to your account 
install python3-venv python3-pip supervisor -y  # gunicorn 
sudo apt-get install python3-venv python3-pip supervisor gunicorn  -y  # 
# create env and active and 
# and clone your project and install requerment filse 
python3 -m venv env 
source  env/bin/activate


git clone djanog 
git clone git@github.com:hamzoooz/themezoz.git
pip install -r requirements.txt 
supervisor 
sudo apt-get install supervisor  
sudo apt-get install nginx 

pip install gunicorn 
## to check every thing it work good or no 
### you must be allow setup djanog and server to allow run in this port 

python manage.py runserver 0.0.0.0:8000

gunicorn  --bind 0.0.0.0:8000 themezoz.wsgi:application

# Step Three Supervisor and gunicorn 
sudo nano /etc/supervisor/conf.d/gunicorn.conf
ubuntu
~~~bach

[program:gunicorn]
directory = /home/hamzoooz/themezoz/themezoz
command = /home/hamzoooz/themezoz/env/bin/gunicorn --workers 3 --bind unix:/home/hamzoooz/themezoz/themezoz/app.sock themezoz.wsgi:application
autostart=true
autorestart=true
stderr_logfile= /var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log
[group:guni]
programs:gunicorn

~~~
sudo mkdir /var/log/gunicorn

# check it work ? 
sudo supervisorctl reread
>> guni: available
sudo supervisorctl update
>> guni: added process group
sudo supervisorctl status 

<!-- cange the user  -->
sudo nano /etc/nginx/nginx.conf
sudo chown hamzoooz:hamzoooz -R /etc/nginx/nginx.conf


#Step Four NGINX 
sudo apt install nginx
sudo nano /etc/nginx/sites-available/djanog.conf

server {
    listen 80;
    server_name themezoz.com www.themezoz.com ;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
	autoindex on;
        alias /home/hamzoooz/themezoz/themezoz/staticfiles/;
    }
    location /media/ {
        alias /home/hamzoooz/themezoz/themezoz/media/;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/hamzoooz/themezoz/themezoz/app.sock;
    }
}

cd /etc/nginx/sites-available/
sudo chown hamzoooz:hamzoooz -R djanog.conf 
sudo ln /etc/nginx/sites-available/themezoz.conf  /etc/nginx/sites-enabled/

sudo service nginx restart
sudo nginx -t 

<!-- go to project dir  -->
<!-- cd /home/hamzoooz/themezoz -->
python manage.py  collectstatic
# Step Five in install Free SSL with certbot 
=======
```



sudo nginx -t
sudo service nginx restart

python manage.py collectstatic
 
sudo apt install certbot python3-certbot-nginx -y 
sudo certbot 




sudo ln -s /etc/nginx/sites-available/djanog.conf /etc/nginx/sites-enabled/







<!-- on digital ocean  -->
ssh root@143.198.149.190
ssh hamzoooz@143.198.149.190

adduser hamzoooz

usermod -aG sudo hamzoooz

ufw app list
ufw allow OpenSSH
ufw enable
ufw status
rsync --archive --chown=hamzoooz:hamzoooz ~/.ssh /home/hamzoooz

sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
Hamzoooz@0784512346#themezoz.com

sudo -u postgres psql

CREATE DATABASE themezoz;

CREATE USER themezoz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';
CREATE USER hamzoooz WITH PASSWORD 'Hamzoooz&0784512346#themezoz.com';

ALTER ROLE themezoz SET client_encoding TO 'utf8';
ALTER ROLE themezoz SET default_transaction_isolation TO 'read committed';
ALTER ROLE themezoz SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE themezoz TO themezoz;
GRANT ALL PRIVILEGES ON DATABASE themezoz TO hamzoooz;

ALTER DATABASE <db_name> OWNER TO <db_user>;
ALTER DATABASE themezoz OWNER TO hamzoooz;
\q

mkdir ~/themezoz
cd ~/themezoz

python3 -m venv env
source env/bin/activate

pip install django gunicorn psycopg2-binary

nano ~/themezoz/myproject/settings.py 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'themezoz',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

~/themezoz/manage.py makemigrations
~/themezoz/manage.py migrate

~/themezoz/manage.py createsuperuser

~/themezoz/manage.py collectstatic

sudo ufw allow 8000
~/themezoz/manage.py runserver 0.0.0.0:8000
http://server_domain_or_IP:8000


cd ~/themezoz
gunicorn --bind 0.0.0.0:8000 themezoz.wsgi
deactivate

sudo nano /etc/systemd/system/gunicorn.socket

    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target

sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=hamzoooz
Group=www-data
WorkingDirectory=/home/hamzoooz/themezoz
ExecStart=/home/hamzoooz/themezoz/env/bin/gunicorn \
        --access-logfile - \
        --workers 3 \
        --bind unix:/run/gunicorn.sock \
        themezoz.wsgi:application

[Install]
WantedBy=multi-user.target



sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl status gunicorn.socket

file /run/gunicorn.sock

sudo journalctl -u gunicorn.socket

sudo systemctl status gunicorn

sudo journalctl -u gunicorn


sudo systemctl daemon-reload
sudo systemctl restart gunicorn


sudo nano /etc/nginx/sites-available/themezoz

server {
    listen 80;
    server_name book-hope.com www.book-hope.com  143.198.149.190 ;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/hamzoooz/themezoz;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }

    location /static/ {
        autoindex on;
        alias /home/ubuntu/themezoz/staticfiles/;
    }
        location /media/ {
        alias /home/ubuntu/themezoz/media/;
    }

}


sudo ln -s /etc/nginx/sites-available/themezoz /etc/nginx/sites-enabled


sudo nginx -t


sudo systemctl restart nginx


sudo ufw allow 8000
sudo ufw allow 'Nginx Full'


sudo tail -F /var/log/nginx/error.log


namei -l /run/gunicorn.sock


sudo systemctl status postgresql


sudo systemctl start postgresql
sudo systemctl enable postgresql


sudo systemctl restart gunicorn


sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service


sudo nginx -t && sudo systemctl restart nginx




chown -R www-data:www-data /var/www/book-hope.com