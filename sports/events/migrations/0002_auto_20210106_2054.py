# Generated by Django 3.1.5 on 2021-01-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Логотип'),
        ),
    ]