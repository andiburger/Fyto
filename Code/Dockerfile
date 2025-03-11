FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]