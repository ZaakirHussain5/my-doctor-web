from apscheduler.schedulers.background import BackgroundScheduler
from schedules import apsjob

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(apsjob.send_todays_message, 'interval', days=1)
    scheduler.start()