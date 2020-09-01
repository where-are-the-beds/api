FROM python:3.7-slim-stretch

COPY *.py /
COPY templates templates/
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["wsgi.py"]