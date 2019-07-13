FROM ubuntu:19.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y cron

COPY crontab.txt /opt
RUN crontab /opt/crontab.txt

#RUN touch /var/log/cron.log
#CMD cron && tail -f /var/log/cron.log
CMD cron -f
