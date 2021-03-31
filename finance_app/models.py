from django.db import models


# Create your models here.
class Headline(models.Model):
    title = models.CharField(max_length=100, unique=True)
    # date = models.DateField()
    head_img = models.URLField(unique=True)
    start_paragraph = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f"{self.title}, {self.start_paragraph}"


class Ticker(models.Model):  # Trebuie legat de Headline + Content pentru vizualizare personalizata
    url = models.TextField()


class Graphs(models.Model):  # Trebuie legat de Ticker
    ticker_graph = models.TextField()  # maybe
