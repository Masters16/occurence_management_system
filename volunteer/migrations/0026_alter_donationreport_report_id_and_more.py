# Generated by Django 4.2.3 on 2023-08-24 03:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0025_alter_donationreport_report_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('eff7b510-f9ef-4a4d-b005-d5abc1b8ee7f'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donorreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('710f6f4d-025a-4b45-bd07-d7ea591c0621'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexamsreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('d0cb246d-dac8-42ab-84cd-8e65fd26c555'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('67b2bfa5-1bdf-443b-948c-5a65abc15a35'), max_length=50, primary_key=True, serialize=False),
        ),
    ]
