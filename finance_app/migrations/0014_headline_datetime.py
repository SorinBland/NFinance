# Generated by Django 3.1.7 on 2021-04-14 17:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0013_delete_graphs'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 17, 39, 36, 38651, tzinfo=utc)),
        ),
    ]