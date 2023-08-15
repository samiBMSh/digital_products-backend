# Generated by Django 4.2.4 on 2023-08-15 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='gateway/', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated_time')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Void'), (10, 'Paid'), (20, 'Error'), (30, 'Canceled'), (31, 'Refund')], db_index=True, default=0, verbose_name='status')),
                ('device_uuid', models.CharField(blank=True, max_length=40, verbose_name='device uuid')),
                ('token', models.CharField(max_length=50)),
                ('phone_number', models.BigIntegerField(db_index=True, validators=[utils.validators.PhoneNumberValidators()], verbose_name='phone number')),
                ('consumed_code', models.PositiveIntegerField(db_index=True, null=True, verbose_name='consumed reference code')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='modification time')),
                ('gateway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='payments.gateway', verbose_name='gateway')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='subscriptions.package', verbose_name='package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
            },
        ),
    ]
