import os
import pika
import sys
import time
import json
import env_var
import utils
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',
                    handlers=[logging.StreamHandler(), logging.FileHandler('system.log')])


class RabbitMQConsumer:
    def __init__(self, durable=True):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=env_var.host, port=env_var.port)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=env_var.queue, durable=durable)

    def callback(self, ch, method, properties, body):
        logging.info(" [+] Received %r " % body)
        if utils.write_to_csv(json.loads(body)):
            time.sleep(2)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # send acknowledgement
        logging.info(" [+] Processed Successfully")



    def start_consuming(self):
        self.channel.basic_qos(
            prefetch_count=1
        )  # worker process a least one job to avoid round robin

        self.channel.basic_consume(
            queue="basic_queue", on_message_callback=self.callback
        )
        logging.info(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()


if __name__ == "__main__":
    try:
        consumer = RabbitMQConsumer()
        consumer.start_consuming()
    except KeyboardInterrupt:
        logging.info("Shutting Down...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
