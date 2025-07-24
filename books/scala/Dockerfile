FROM ubuntu:20.10
RUN apt update                  && \
    apt install -y less         && \
    apt install -y scala        && \
    apt install -y vim          && \
    apt install -y curl         && \
    apt install -y gnupg        && \
    echo DONE

RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list                                    && \
    curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | apt-key add   && \
    apt update          && \
    apt install -y sbt  && \
    echo DONE

RUN rm -rf /var/lib/apt/lists/* && \
    echo DONE cleanup

WORKDIR /opt
