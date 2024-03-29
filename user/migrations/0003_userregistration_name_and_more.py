# Generated by Django 4.2.3 on 2023-08-23 20:09

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userregistration_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='name',
            field=models.CharField(default='Name', max_length=20),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 23, 9, 43, 562316)),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='user_no',
            field=models.CharField(default=uuid.UUID('d2246951-628c-406c-9f91-9772d5ee31cc'), max_length=40, primary_key=True, serialize=False),
        ),
    ]
