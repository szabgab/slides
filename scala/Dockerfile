FROM ubuntu:20.10
RUN apt update                  && \
    apt install -y less         && \
    apt install -y scala        && \
    apt install -y default-sdk  && \
    apt install -y vim          && \
    echo DONE

#RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
#    apt install gnupg -y && \
#    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv                             && \
#    apt update      && \
#    apt install sbt -y  && \
#    echo DONE

RUN rm -rf /var/lib/apt/lists/* && \
    echo DONE cleanup

WORKDIR /opt
