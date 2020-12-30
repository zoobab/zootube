FROM python:3.6.12-alpine3.12
RUN apk add ffmpeg youtube-dl py3-flask
COPY . /app
WORKDIR /app
ENTRYPOINT FLASK_APP=zootube.py flask run --host=0.0.0.0
