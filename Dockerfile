FROM python:3.11-slim

EXPOSE 5001

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \
    libsndfile1-dev \
    portaudio19-dev \
    ffmpeg \
    && apt-get clean \
    python3 \
    python3-dev \
    python3-pip \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["python", "/app/app/app.py"]