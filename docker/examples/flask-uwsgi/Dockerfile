FROM ubuntu:19.10
RUN apt-get update                          && \
    apt-get upgrade -y                      && \
    apt-get install -y python3              && \
    apt-get install -y uwsgi                && \
    apt-get install -y uwsgi-plugin-python3

RUN apt-get install -y python3-pip

COPY . /opt/
RUN pip3 install -r /opt/requirements.txt

COPY uwsgi.ini /etc/uwsgi/apps-enabled/

WORKDIR /opt

CMD service uwsgi start; tail -F /var/log/uwsgi/app/uwsgi.log

