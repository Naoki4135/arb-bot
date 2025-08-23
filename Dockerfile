FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 TZ=Asia/Tokyo
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "run_notifier.py"]

