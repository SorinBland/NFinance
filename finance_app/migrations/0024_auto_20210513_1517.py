# Generated by Django 3.1.7 on 2021-05-13 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0023_delete_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticker',
            name='company_address',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='company_address2',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='company_website',
        ),
    ]
