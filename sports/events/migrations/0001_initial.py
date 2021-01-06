# Generated by Django 3.1.5 on 2021-01-06 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Спонсор',
                'verbose_name_plural': 'Спонсоры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('prize_fund', models.IntegerField(verbose_name='Призовой фонд')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sponsor', verbose_name='Спонсор')),
            ],
            options={
                'verbose_name': 'Турнир',
                'verbose_name_plural': 'Турниры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('time', models.DateTimeField(verbose_name='Время проведения')),
                ('result', models.CharField(blank=True, max_length=64, verbose_name='Результат')),
                ('status', models.CharField(max_length=64, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Категория')),
                ('teams', models.ManyToManyField(to='teams.Team', verbose_name='Команды')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['name'],
            },
        ),
    ]
