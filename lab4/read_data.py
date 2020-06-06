import datetime
import redis
import requests

from export_configuration import ExportSourceSelector
from settings import settings


class Data:
    """
    Data class
    """
    COMPLETED_STATUS = 'COMPLETED'

    def __init__(self, url):
        """
        Initialize data
        """
        self.url = url

    def read(self):
        """
        Read data from url
        """
        rows_count = 0
        redis_db = redis.Redis(host=settings.CONFIG['REDIS_HOST'], port=settings.CONFIG['REDIS_PORT'], db=0)
        current_time = str(datetime.datetime.now())

        if redis_db.lindex(self.url, 0):
            data_status = redis_db.lindex(self.url, 0).decode('utf-8')
        else:
            data_status = ''

        if data_status == self.COMPLETED_STATUS:
            print('Try to load existing data')
        else:
            data = requests.get(self.url).json()
            redis_db.lpush(self.url, current_time)

            for row in data:
                rows_count += 1
                application_number = row.get('ApplicationNumber')
                company_address = row.get('CompanyAddress')
                company_city = row.get('CompanyCity')
                company_name = row.get('CompanyName')

                first_submission_date = row.get('FirstSubmissionDate')
                property_type = row.get('PropertyType')
                location = row.get('Location 1')
                total_cost = row.get('TotalCost')

                export_source = ExportSourceSelector()
                export_source.send_data(application_number, company_address, company_city, company_name, first_submission_date,
                          property_type, location, total_cost, rows_count)

                if rows_count % 100 == 0:
                    redis_db.lpush(self.url, f'{rows_count - 99}-{rows_count}')
            redis_db.lpush(self.url, self.COMPLETED_STATUS)
