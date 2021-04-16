from django.apps import AppConfig


class FinanceAppConfig(AppConfig):
    name = 'finance_app'

    def ready(self):
        from finance_app.scraper import scrape
        from apscheduler.schedulers.background import BackgroundScheduler
        print('Initializing scheduler')
        scheduler = BackgroundScheduler()
        scheduler.add_job(scrape, 'interval', minutes=10)
        scheduler.start()
