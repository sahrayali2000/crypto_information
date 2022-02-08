from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from webscraping import webscraping


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(webscraping.market_info, 'interval', minutes=1440)
    scheduler.start()
