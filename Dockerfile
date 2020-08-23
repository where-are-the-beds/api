FROM alpine:3.12

RUN apk update && apk add py3-flask py3-gunicorn nginx supervisor

COPY wsgi.py . 
COPY nginx.conf /etc/nginx/conf.d/
COPY supervisord.conf .

EXPOSE 80

ENTRYPOINT ["supervisord", "-c", "supervisord.conf" ]