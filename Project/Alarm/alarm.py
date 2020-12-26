from twilio.rest import Client
from datetime import datetime
import time

TWILIO_ACCOUNT_SID = 'private'
TWILIO_AUTH_TOKEN = 'private'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

year, month, day, hour, minute, second = map(int, input().split())

if hour <= 12:
    hour += 12

while True:
    now = datetime.now()
    print("{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    ))
    time.sleep(1)
    if now.year == year and now.month == month and now.day == day and now.hour == hour and now.minute == minute and \
            now.second == second:
        print("Alarm Message Sent!")
        client.messages.create(to="private", from_="private", body="Alarm!")
        year, month, day, hour, minute, second = map(int, input().split())