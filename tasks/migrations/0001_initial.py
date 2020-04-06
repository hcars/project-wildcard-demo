# Generated by Django 3.0.3 on 2020-04-05 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=-1)),
                ('task_name', models.CharField(max_length=200)),
                ('task_desc', models.CharField(max_length=400)),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('length', models.DurationField(default=datetime.timedelta(seconds=10800), verbose_name='length')),
                ('completed', models.BooleanField(verbose_name='completed')),
                ('date_completed', models.DateField(null=True, verbose_name='date_completed')),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('link', models.URLField(default='')),
                ('category', models.CharField(blank=True, choices=[('Homework', 'Homework'), ('Chore', 'Chore'), ('Work', 'Work'), ('Errand', 'Errand'), ('Life', 'Lifestyle'), ('Other', 'Others')], max_length=32, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
