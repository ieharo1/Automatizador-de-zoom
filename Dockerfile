FROM python:3.12-slim
WORKDIR /app
COPY controller/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY controller/app.py .
EXPOSE 7000
CMD ["python", "app.py"]
