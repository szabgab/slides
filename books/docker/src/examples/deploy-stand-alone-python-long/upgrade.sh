docker build -t flasker .
docker container stop flask
docker container rm flask
docker run -d --name flask -v/data:/data --env COUNTER_DIR=/data --restart unless-stopped  -p5000:5000 flasker

