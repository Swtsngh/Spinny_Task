FROM ubuntu:18.04
MAINTAINER swtsngh731@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY requirements.txt requirements.txt
COPY flaskapp /opt/

RUN pip3 install -r requirements.txt
WORKDIR /opt/

CMD ["gunicorn3", "-b", "54.193.19.130:8000", "app:app", "--workers=5"]
