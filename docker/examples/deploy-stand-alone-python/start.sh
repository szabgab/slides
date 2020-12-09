docker build -t flasker .
docker run -d --name flask --restart unless-stopped  -p5000:5000 flasker

