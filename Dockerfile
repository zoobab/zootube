FROM python:3.6.12-alpine3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
