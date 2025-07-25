# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY index.py .

RUN pip install requests

CMD ["python", "index.py"]
