# Generated by Django 3.1.7 on 2021-05-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0018_auto_20210505_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='company_logo',
            field=models.URLField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='company_website',
            field=models.URLField(blank=True, default=1, null=True),
        ),
    ]
