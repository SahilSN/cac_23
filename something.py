import datetime
import pandas as pd
from datetime import datetime, timedelta

def return_dates():
    now=datetime.now().replace(microsecond=0).replace(second=0)

    DATE_TIME_STRING_FORMAT = '%Y-%m-%d %H:%M:%S'

    from_date_time = datetime.strptime('2023-06-06 05:00:00',
                                       DATE_TIME_STRING_FORMAT)
    to_date_time = datetime.strptime(str(now),
                                     DATE_TIME_STRING_FORMAT)

    date_times = [from_date_time.strftime(DATE_TIME_STRING_FORMAT)]
    date_time = from_date_time
    while date_time < to_date_time:
        date_time += timedelta(minutes=15)
        date_times.append(date_time.strftime(DATE_TIME_STRING_FORMAT))
    return date_times

print(return_dates())

def add_to_csv(datetimes):
    return