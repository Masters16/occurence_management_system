# Generated by Django 4.2.3 on 2023-08-23 19:57

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0039_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A', 'A'), ('O-', 'O-'), ('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('B-', 'B-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 22, 57, 18, 62039)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('b27113cd-8e5b-4a3c-8fb6-6e1c3de06fd2'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Platelets', 'Platelets'), ('Plasma', 'Plasma'), ('Power Red', 'Power Red'), ('Blood', 'Blood')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A', 'A'), ('O-', 'O-'), ('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('B-', 'B-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kilifi', 'Kilifi'), ('Kakamega', 'Kakamega'), ('Nandi', 'Nandi'), ('Bungoma', 'Bungoma'), ('Kajiado', 'Kajiado'), ('Mandera', 'Mandera'), ('Uasin Gishu', 'Uasin Gishu'), ('Nakuru', 'Nakuru'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Migori', 'Migori'), ('West Pokot', 'West Pokot'), ('Vihiga', 'Vihiga'), ('Turkana', 'Turkana'), ('Machakos', 'Machakos'), ('Busia', 'Busia'), ('Garissa', 'Garissa'), ('Isiolo', 'Homa Bay'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Kirinyaga', 'Kirinyaga'), ('Nyeri', 'Nyeri'), ('Nyandarua', 'Nyandarua'), ('Tana River', 'Tana River'), ('Kwale', 'Kwale'), ('Kiambu', 'Kiambu'), ('Marsabit', 'Marsabit'), ('Homa Bay', 'Homa Bay'), ('Nairobi', 'Nairobi'), ('Narok', 'Narok'), ('Kisii', 'Kisii'), ('Embu', 'Embu'), ('Samburu', 'Samburu'), ('Wajir', 'Wajir'), ('Kitui', 'Kitui'), ('Kisumu', 'Kisumu'), ('Nyamira', 'Nyamira'), ('Siaya', 'Siaya'), ('Meru', 'Meru'), ('Trans Nzoia', 'Trans Nzoia'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ("Murang'a", "Murang'a"), ('Kericho', 'Kericho'), ('Makueni', 'Makueni'), ('Baringo', 'Baringo'), ('Bomet', 'Bomet')], default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 22, 57, 18, 53045)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('998743ce-8200-4710-a201-06d0a6eca5ff'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A', 'A'), ('O-', 'O-'), ('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('B-', 'B-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('Nil', 'Nil'), ('M', 'M'), ('F', 'F')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 22, 57, 18, 64037)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 22, 57, 18, 60039)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('0c8f4bbd-21f5-496c-8dc6-5ebf7d464751'), max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=8),
        ),
    ]
