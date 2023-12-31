# Generated by Django 4.2.4 on 2023-08-15 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 7, 9, 27, 840880, tzinfo=datetime.timezone.utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address', null=True),
        ),
    ]
