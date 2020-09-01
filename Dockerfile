FROM alpine:3.12

RUN apk add --no-cache py3-flask

COPY wsgi.py . 

EXPOSE 80

ENTRYPOINT ["python3"]
CMD ["wsgi.py"]