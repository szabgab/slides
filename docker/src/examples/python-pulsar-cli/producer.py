import pulsar
import time
from mytools import get_logger, topic


def send():
    logger = get_logger('pulsar')
    logger.info("Producer starting")
    time.sleep(20)
    logger.info("Producer really starting")

    filename = 'input.txt'

    try:
        client = pulsar.Client('pulsar://my-pulsar:6650')
        producer = client.create_producer(topic)
    except Exception:
        logger.exception("Producer could not connect to pulsar")
    logger.info("Producer connected")

    with open(filename) as fh:
        for row in fh:
            logger.info(f"Sending {row}")
            producer.send(row.encode('utf-8'))
            time.sleep(1)

send()
