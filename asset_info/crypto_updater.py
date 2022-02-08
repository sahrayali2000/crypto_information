from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from asset_info import get_info


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_info.crypto_information, 'interval', minutes=1440)
    scheduler.start()
