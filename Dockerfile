FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "app.api.routes:router", "--host", "0.0.0.0", "--port", "8000"]