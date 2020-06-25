# Blog Site
This is a [blog site](https://blog.f1recloud.com/) I have created for myself and some friends. However, feel free to signup and create your own posts on there! You can also host this yourself if you'd like.

# Setup
Just make sure you have docker and docker-compose installed on your system. There are lots of tutorials out there on the internet on how to install them. 

Once you have those both installed, run this command: `docker-compose up` And that's it! The site should be up and running.

You will have to edit some of the configuration files to get it working specifically for your server though, specifically [scripts/nginx/nginx.conf](https://github.com/Den4200/blog_site/blob/master/scripts/nginx/nginx.conf), [blog_site/settings.py](https://github.com/Den4200/blog_site/blob/master/blog_site/settings.py), and optionally [scripts/uwsgi.ini](https://github.com/Den4200/blog_site/blob/master/scripts/uwsgi.ini).
