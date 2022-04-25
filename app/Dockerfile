FROM python:latest

WORKDIR /app

COPY Requirements.txt /app

RUN pip install -r Requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

