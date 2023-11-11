FROM python:3.11-slim-buster

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt .

# Path: /app
RUN pip install -r requirements.txt

# Path: /app
COPY . .

EXPOSE 8080

# Path: /app
CMD ["python", "main.py"]