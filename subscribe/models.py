from django.db import models


# Create your models here.


class SubEmails(models.Model):
    email = models.EmailField(unique=True)
    uuid = models.CharField(max_length=9999, null=True, blank=True)

    def __str__(self):
        return self.email
