FROM ubuntu:20.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3

RUN apt-get install -y python3-pip

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
CMD FLASK_APP=app FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 5000
