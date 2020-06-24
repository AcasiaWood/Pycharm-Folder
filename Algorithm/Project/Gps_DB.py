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

    now = '{0}-{1}-{2}'.format(date.year, date.month, date.day)

    with conn.cursor() as curs:
        sql = "insert into gps values (%s, %s, %s, %s)"
        curs.execute(sql, (id, now, latitude, longitude))
        conn.commit()
        print("\n정보 입력에 성공했습니다.\n")

    id += 1
