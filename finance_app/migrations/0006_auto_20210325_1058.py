# Generated by Django 3.1.7 on 2021-03-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0005_remove_headline_title2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='head_img',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='start_paragraph',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
