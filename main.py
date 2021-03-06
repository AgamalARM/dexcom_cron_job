from datetime import datetime
import requests

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    x = requests.get('http://dexcom.invasso.com/api/dexcom/simulation', headers=headers)
    y = x.json()
    print(y)
    print("*************************************************************************")
    trend_name = y['trend']
    reading_value =  y['sensor_treading_value']
    student_id = y['student_id']
