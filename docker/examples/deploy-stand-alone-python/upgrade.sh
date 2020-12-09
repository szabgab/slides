docker build -t flasker .
docker container stop flask
docker container rm flask
docker run -d --name flask --restart unless-stopped  -p5000:5000 flasker

