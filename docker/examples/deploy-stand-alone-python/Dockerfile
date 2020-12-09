FROM python:3.7
COPY requirements.txt /opt/
COPY app.py /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
#CMD FLASK_APP=app FLASK_DEBUG=1 flask run --host 0.0.0.0 --port 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

