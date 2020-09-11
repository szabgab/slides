FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y curl

CMD ["--silent", "http://httpbin.org/get"]
ENTRYPOINT ["curl"]
