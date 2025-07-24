FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y cron

COPY crontab.txt /opt
RUN crontab /opt/crontab.txt

RUN touch /opt/jumanji.txt
CMD ["cron", "&&", "tail", "-f", "/opt/jumanji.txt"]
