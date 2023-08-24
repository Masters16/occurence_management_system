# Generated by Django 4.2.3 on 2023-08-23 17:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('police', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurencerecords',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 991658)),
        ),
        migrations.AlterField(
            model_name='occurencerecords',
            name='record_id',
            field=models.CharField(default=uuid.UUID('876f31c3-94b0-45a2-a9b0-ab2cd7dad97b'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='occurencerecords',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='occurencerecords',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userregistration'),
        ),
        migrations.AlterField(
            model_name='policeregistration',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 989659)),
        ),
        migrations.AlterField(
            model_name='policeregistration',
            name='police_id',
            field=models.CharField(default=uuid.UUID('b47fcd33-8721-4030-84ab-138f1f15b834'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.CharField(default=uuid.UUID('be0a9fd4-d572-4bea-89ae-f65c17eb9ade'), max_length=40, primary_key=True, serialize=False),
        ),
    ]
