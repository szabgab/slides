FROM amazonlinux
RUN yum install -y python36
RUN yum install -y findutils which wget

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

WORKDIR /opt

