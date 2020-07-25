import pymysql
import time
from datetime import datetime

conn = pymysql.connect(host='private', user='private', password='private', db='gps', charset='utf8')

id = 1
date = datetime.now()
latitude = 100
longitude = 100

while True:

    time.sleep(1)

    period = "{0}-{1}-{2}".format(date.year, date.month, date.day)

    with conn.cursor() as curs:
        sql = "insert into gps values (%s, %s, %s, %s)"
        curs.execute(sql, (id, period, latitude, longitude))
        conn.commit()
        print("\Information was inputted successfully.\n")

    id += 1
