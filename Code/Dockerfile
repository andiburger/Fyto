FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Command to start the application (ensuring the virtual environment is activated)
CMD ["/bin/bash", "-c", ". venv/bin/activate && python main.py"]