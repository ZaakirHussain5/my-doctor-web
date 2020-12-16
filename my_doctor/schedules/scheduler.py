from apscheduler.schedulers.background import BackgroundScheduler
from schedules import apsjob

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_todays_message, 'interval', days=1)
    scheduler.start()


def every_15mins_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_message_before_15mins, 'interval', minutes=1)
    scheduler.start()

def every_10mins_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_message_before_10mins, 'interval', minutes=1)
    scheduler.start()

def every_5mins_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_message_before_5mins, 'interval', minutes=1)
    scheduler.start()
