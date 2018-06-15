FROM alpine:3.7
RUN apk update && \
    apk add zip gcc g++ make zlib zlib-dev && \
    apk add python3 python3-dev
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py



# RUN apk update && \
#     apk add zip gcc g++ make zlib zlib-dev
# # build-base
# 
# RUN wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz && \
#     tar -xzvf Python-3.6.1.tgz && \
#     cd Python-3.6.1 && \
#     ./configure && \
#     make && \
#     make install

