from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig

from finance_app.scraper import scrape


class FinanceAppConfig(AppConfig):
    name = 'finance_app'

    def ready(self):
        print('Initializing scheduler')
        scheduler = BackgroundScheduler()
        scheduler.add_job(scrape, 'interval', second=30)
        scheduler.start()



