FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y cron

COPY crontab.txt /opt
RUN crontab /opt/crontab.txt

CMD ["cron", "-f"]
