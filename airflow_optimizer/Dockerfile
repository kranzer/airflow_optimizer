FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
RUN pytest tests/

EXPOSE 5555
CMD ["python", "app.py"]