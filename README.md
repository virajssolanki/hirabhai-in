gunicorn --bind 0.0.0.0:8000 pillow.wsgi
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

sudo nano /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo systemctl restart nginx

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04


admin
#viraz@171198

virazssolanki@gmail.com
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


8 hours 
4 hours 