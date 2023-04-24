FROM python:3.6-slim

WORKDIR /consumer_backend

COPY . /consumer_backend

COPY requirements.txt /consumer_backend

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "consumer.py"]
