import logging

from export_source import ExportSource


class Log(ExportSource):
    """
    Log class
    """
    def __init__(self):
        super(ExportSource, self).__init__()

    @staticmethod
    def send_data(application_number, company_address, company_city, company_name, first_submission_date,
                  property_type, location, total_cost, row_id):
        """
        Log data into console
        """
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.info(f'LOG DATA FOR {row_id} ROW')
        logging.info(f'APPLICATION_NUMBER={application_number}')
        logging.info(f'COMPANY_ADDRESS={company_address}')
        logging.info(f'COMPANY_CITY={company_city}')
        logging.info(f'COMPANY_NAME={company_name}')
        logging.info(f'FIRST_SUBMISSION_DATE={first_submission_date}')
        logging.info(f'PROPERTY_TYPE={property_type}')
        logging.info(f'LOCATION={location}')
        logging.info(f'TOTAL_COST={total_cost}')
        logging.info('.............................................................')
