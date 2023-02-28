FROM ubuntu:22.10
RUN apt-get update
RUN apt-get install -y curl

ENTRYPOINT ["curl"]   # fixed
CMD ["--silent", "http://httpbin.org/get"]  # replacable
