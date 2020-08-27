FROM alpine:3.12

RUN apk add --no-cache \
		py3-flask \
	    py3-gunicorn \
		nginx \
		supervisor \
        py-pip

RUN pip install awscli
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION=us-east-1

RUN aws s3 sync s3://where-are-the-beds/usa-hospital-beds/dataset/ dataset/

COPY wsgi.py . 
COPY nginx.conf /etc/nginx/conf.d/
COPY supervisord.conf .

EXPOSE 80

ENTRYPOINT ["supervisord", "-c", "supervisord.conf" ]