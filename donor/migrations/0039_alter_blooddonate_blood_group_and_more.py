# Generated by Django 4.2.3 on 2023-08-23 17:42

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0038_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('O-', 'O-'), ('AB+', 'AB+'), ('O+', 'O+'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 955679)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('fcbe8401-5500-44b8-aa91-667a6774d9ee'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Blood', 'Blood'), ('Plasma', 'Plasma'), ('Platelets', 'Platelets'), ('Power Red', 'Power Red')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A', 'A'), ('O-', 'O-'), ('AB+', 'AB+'), ('O+', 'O+'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='county',
            field=models.CharField(choices=[('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Siaya', 'Siaya'), ('Nyamira', 'Nyamira'), ('Garissa', 'Garissa'), ('Mombasa', 'Mombasa'), ('Migori', 'Migori'), ('Isiolo', 'Homa Bay'), ('Bomet', 'Bomet'), ('Nandi', 'Nandi'), ('Kiambu', 'Kiambu'), ('Vihiga', 'Vihiga'), ('Nyandarua', 'Nyandarua'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Kilifi', 'Kilifi'), ('Samburu', 'Samburu'), ('Taita-Taveta', 'Taita-Taveta'), ('Embu', 'Embu'), ('Trans Nzoia', 'Trans Nzoia'), ('Laikipia', 'Laikipia'), ('Kwale', 'Kwale'), ('Homa Bay', 'Homa Bay'), ('West Pokot', 'West Pokot'), ('Busia', 'Busia'), ('Makueni', 'Makueni'), ('Kitui', 'Kitui'), ('Kisii', 'Kisii'), ("Murang'a", "Murang'a"), ('Mandera', 'Mandera'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nyeri', 'Nyeri'), ('Wajir', 'Wajir'), ('Kericho', 'Kericho'), ('Baringo', 'Baringo'), ('Machakos', 'Machakos'), ('Kakamega', 'Kakamega'), ('Turkana', 'Turkana'), ('Kirinyaga', 'Kirinyaga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Uasin Gishu', 'Uasin Gishu'), ('Nairobi', 'Nairobi'), ('Bungoma', 'Bungoma'), ('Meru', 'Meru'), ('Marsabit', 'Marsabit'), ('Narok', 'Narok'), ('Nakuru', 'Nakuru')], default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 949683)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('b239e10f-fb5a-4b97-81c7-563ea4fe51fb'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('O-', 'O-'), ('AB+', 'AB+'), ('O+', 'O+'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M'), ('Nil', 'Nil')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 956679)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 952680)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('599f6b9c-4fd8-43b0-930c-807f770614ba'), max_length=10, primary_key=True, serialize=False),
        ),
    ]
