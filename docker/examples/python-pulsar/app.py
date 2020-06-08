from flask import Flask, request, render_template
import datetime
import pulsar

app = Flask(__name__)

topic = "name"

client = pulsar.Client('pulsar://my-pulsar:6650')
consumer = client.subscribe(topic, 'my-subscription')
producer = client.create_producer(topic)


@app.route("/")
def main():
    app.logger.info("main")
    return render_template('main.html')


@app.route("/save", methods=['POST'])
def save():
    value = request.form['value']
    app.logger.info(f"to save: {value}")

    producer.send(value.encode('utf-8'))
    app.logger.info("sent message")
    return render_template('main.html', saved=1, value=value)

@app.route("/get", methods=['POST'])
def get():

    app.logger.info("consumer")
    msg = consumer.receive()
    app.logger.info("received")
    try:
        value = "{}: {}".format(msg.data(), msg.message_id())
        consumer.acknowledge(msg)
    except Exception as err:
        value = f"Exception {err}"
    app.logger.info(f"value: {value}")

    return render_template('main.html', value=value)
