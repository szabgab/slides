FROM ubuntu:20.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3

RUN apt-get install -y python3-pip
RUN pip3 install requests

COPY curl.py /opt/

ENTRYPOINT ["/opt/curl.py"]

