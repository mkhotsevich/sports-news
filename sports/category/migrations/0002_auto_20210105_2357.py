# Generated by Django 3.1.5 on 2021-01-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
    ]