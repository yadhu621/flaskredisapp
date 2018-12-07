FROM python:2.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5000

ENV FLASK_APP app.py

ENTRYPOINT flask run --host='0.0.0.0'
