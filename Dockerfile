FROM alpine:3.12

COPY src/ .
COPY requirements.txt .

RUN apk add --no-cache py3-flask py3-pip
RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["wsgi.py"]