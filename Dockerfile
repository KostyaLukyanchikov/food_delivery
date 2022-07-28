FROM python:3.10.5-slim-buster

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# COPY src/entrypoint.sh entrypoint.sh


COPY /src /app
WORKDIR /app

RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

ENV PYTHONUNBUFFERED=1

CMD sh entrypoint.sh
