docker build -t mydocker .
docker run -it --name app --rm -p:5001:5000 -v $(pwd):/opt/  mydocker


http://localhost:5001/
