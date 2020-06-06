import json
from kafka import KafkaProducer
from time import sleep

from export_source import ExportSource
from settings import settings


class Kafka(ExportSource):
    """
    Kafka class
    """
    def __init__(self):
        super(ExportSource, self).__init__()

    @staticmethod
    def send_data(application_number, company_address, company_city, company_name, first_submission_date,
                  property_type, location, total_cost, row_id):
        """
        Send data to kafka topic
        """

        producer = KafkaProducer(
            bootstrap_servers=[f"{settings.CONFIG['KAFKA_HOST']}:{settings.CONFIG['KAFKA_PORT']}"],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        data = {'id': row_id,
                'application_number': application_number,
                'company_address': company_address,
                'company_city': company_city,
                'company_name': company_name,
                'first_submission_date': first_submission_date,
                'property_type': property_type,
                'location': location,
                'total_cost': total_cost}

        if settings.CONFIG['KAFKA_TOPIC_ID'] == 1:
            topic_name = 'topic1'
        else:
            topic_name = 'topic3'
        producer.send(topic_name, data)
        sleep(0.1)
