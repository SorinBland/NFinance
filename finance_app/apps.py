from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.apps import AppConfig
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore

from finance_app import scraper


class FinanceAppConfig(AppConfig):
    name = 'finance_app'

    def ready(self):

        print('Initializing scheduler')
        scheduler = BackgroundScheduler(BlockingScheduler(timezone=settings.TIME_ZONE))
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(scraper.scrape,
                          trigger=CronTrigger(second="*/10"),
                          id='scrape',
                          max_instances=1,
                          replace_existing=False)
        scheduler.start()


