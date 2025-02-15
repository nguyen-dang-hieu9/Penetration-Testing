FROM python:3.12
EXPOSE 3000
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "2", "--timeout", "90", "--preload", "app:app"]
