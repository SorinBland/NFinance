# Generated by Django 3.1.7 on 2021-05-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subemails',
            name='choice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
