from apscheduler.schedulers.background import BackgroundScheduler
from schedules import apsjob
from schedules import planScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_todays_message, 'interval', days=1)
    scheduler.start()

def every_10mins_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_message_before_10mins, 'interval', minutes=1)
    scheduler.start()

def every_5mins_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_message_before_5mins, 'interval', minutes=1)
    scheduler.start()

def appointmentExpiry_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.appointmentExpired, 'interval', minutes=1)
    scheduler.start()


def plan_call():
    scheduler = BackgroundScheduler()
    scheduler.add_job(planScheduler.check_subscription, 'interval', days=1)
    scheduler.start()