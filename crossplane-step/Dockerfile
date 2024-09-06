FROM python:3.12-alpine
RUN apk add --no-cache git curl openssl
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /work
COPY main.py main.py
CMD ["python", "main.py"]