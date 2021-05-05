from django.apps import AppConfig


# Scheduling the scraper to scrape every 10 minutes
class FinanceAppConfig(AppConfig):
    name = 'finance_app'

    # def ready(self):
    #     from finance_app.scraper import scrape, scrape_wsj
    #     from apscheduler.schedulers.background import BackgroundScheduler
    #     print('Initializing scheduler')
    #     scheduler = BackgroundScheduler()
    #     scheduler.add_job(scrape, 'interval', minutes=10)
    #     scheduler.add_job(scrape_wsj, 'interval', minutes=10)
    #     scheduler.start()
