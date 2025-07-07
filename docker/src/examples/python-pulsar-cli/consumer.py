import pulsar
import time
from mytools import get_logger, topic

def receive():
    logger = get_logger('pulsar')
    logger.info('Consumer starting')
    time.sleep(20)
    logger.info('Consumer really starting')

    try:
        client = pulsar.Client('pulsar://my-pulsar:6650')
        consumer = client.subscribe(topic, 'my-subscription')
    except Exception:
        logger.exception("Consumer could not connect to pulsar")
    logger.info("Consumer connected")


    while True:
        msg = consumer.receive()
        try:
            logger.info("Received: {}: {}".format(msg.data(), msg.message_id()))
            consumer.acknowledge(msg)
        except Exception as err:
            logger.error(f"Exception {err}")


receive()
