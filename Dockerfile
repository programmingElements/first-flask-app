FROM python:3.10-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python3", "run.py"]