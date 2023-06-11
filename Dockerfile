FROM python:3.8-buster

RUN pip3 install flask flask_restful

WORKDIR /app

COPY hello.py /app

CMD ["python3", "hello.py"]