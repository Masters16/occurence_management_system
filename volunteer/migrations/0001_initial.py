# Generated by Django 4.2.3 on 2023-07-17 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0028_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationReport',
            fields=[
                ('report_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('station_id', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(default='Donation-report', max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('created_at', models.DateTimeField()),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.volunteerregistration')),
            ],
        ),
    ]