# Generated by Django 3.1.7 on 2021-04-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0010_auto_20210412_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='tick',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
