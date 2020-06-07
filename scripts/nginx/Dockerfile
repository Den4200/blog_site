FROM nginx

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
ENV NGINX_MAX_UPLOAD 100m

# link
ADD scripts/nginx/nginx.conf /etc/nginx/nginx.conf

COPY scripts/nginx/uwsgi_params .
