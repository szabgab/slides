from flask import Flask, request, render_template
import datetime
import pulsar

app = Flask(__name__)



@app.route("/")
def main():
    app.logger.info("main")
    return render_template('main.html')


@app.route("/save", methods=['POST'])
def save():
    topic = request.form['topic']
    value = request.form['value']
    app.logger.info(f"to save: {topic} - {value}")

    client = pulsar.Client('pulsar://my-pulsar:6650')
    producer = client.create_producer(topic)
    res = producer.send(value.encode('utf-8'))
    app.logger.info(f"result: {res}")
    client.close()
    return render_template('main.html', saved=1, value=f"{topic}: {value}")

@app.route("/get", methods=['POST'])
def get():
    topic = request.form['topic']

    client = pulsar.Client('pulsar://my-pulsar:6650')
    consumer = client.subscribe(topic, 'my-subscription')
    app.logger.info("consumer")
    msg = consumer.receive()
    app.logger.info("received")
    try:
        value = "{}: {}".format(msg.data(), msg.message_id())
        consumer.acknowledge(msg)
    except Exception as err:
        value = f"Exception {err}"
    client.close()
    app.logger.info(f"value: {value}")

    return render_template('main.html', field=field, value=value)
