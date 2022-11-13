sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo systemctl restart nginx

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04