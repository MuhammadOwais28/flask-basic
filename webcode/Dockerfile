FROM ubuntu

WORKDIR /app

COPY . .

EXPOSE 80

RUN apt-get update -y
RUN apt-get install python3 python3-pip python3-flask -y && \
apt-get clean

CMD ["python3","app.py"]
