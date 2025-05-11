FROM python:3.11-slim

WORKDIR /app

COPY app.py ./
COPY requirements.txt ./
COPY templates/ ./templates/

RUN pip install --no-cache-dir -r requirements.txt
#port
EXPOSE 5000

CMD ["python", "app.py"]

