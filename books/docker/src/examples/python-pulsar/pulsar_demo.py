mport pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', subscription_name='my-sub')

# while True:
#     msg = consumer.receive()
#     print("Received message: '{}'".format(msg.data())
#     consumer.acknowledge(msg)

client.close()

