FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN apt-get update && apt-get install -y openssh-client && rm -rf /var/lib/apt/lists/*
CMD ["python", "app.py"]