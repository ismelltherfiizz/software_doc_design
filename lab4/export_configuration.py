import kafka_producer
import logs
from settings import settings


class ExportSourceSelector:
    """
    Selector for export source
    """

    def __init__(self):
        """
        Initialize export type mapper for selector
        """
        self.EXPORT_TYPE_MAPPER = {
            'kafka': kafka_producer.Kafka,
            'logs': logs.Log
        }

    def send_data(self, application_number, company_address, company_city, company_name, first_submission_date,
                  property_type, location, total_cost, row_id):
        """
        Send data to export source based on selector
        """
        export_source_name = settings.CONFIG['EXPORT_SOURCE']

        self.EXPORT_TYPE_MAPPER[export_source_name].send_data(application_number, company_address, company_city,
                                                              company_name, first_submission_date,
                                                              property_type, location, total_cost, row_id)
