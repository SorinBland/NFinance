# Generated by Django 3.1.7 on 2021-05-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0015_auto_20210414_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='previous_close',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
