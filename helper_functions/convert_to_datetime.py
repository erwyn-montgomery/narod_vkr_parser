from dateutil import parser
from datetime import datetime


def convert_to_timestamp(date_str):
    try:
        datetime_obj = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        datetime_obj = parser.parse(date_str)
    datetime_obj = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return datetime_obj