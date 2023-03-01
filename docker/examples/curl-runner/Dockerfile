FROM ubuntu:22.10
RUN apt-get update
RUN apt-get install -y curl

ENTRYPOINT ["curl"]   # fixed part
CMD ["--silent", "https://httpbin.org/get"]  # replacable part
