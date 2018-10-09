FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY tasks.py .
CMD celery -A tasks worker --loglevel=info