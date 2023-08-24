# Generated by Django 4.2.3 on 2023-08-23 20:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0024_alter_donationreport_report_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('30b74aaa-6a58-4478-95e0-a6cb24d51b54'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donorreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('502a6af0-c82c-488c-8a0f-e5dda55176ea'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexamsreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('67b53c7f-3298-4286-9a5c-598c4eae9fc0'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('fd7551c0-d38c-4cfb-92fd-5e869efed96c'), max_length=50, primary_key=True, serialize=False),
        ),
    ]
