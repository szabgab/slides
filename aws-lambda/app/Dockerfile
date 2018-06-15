FROM alpine:3.7
RUN apk update && \
    apk add zip gcc g++ make zlib zlib-dev && \
    apk add python3 python3-dev
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

WORKDIR /opt

