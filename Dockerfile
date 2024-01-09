FROM python:3.10-slim

WORKDIR /model

COPY model/. /model

WORKDIR /app

ENV FLASK_RUN_HOST=0.0.0.0

COPY app/app.py /app

COPY app/requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]