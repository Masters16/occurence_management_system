# Generated by Django 4.2.3 on 2023-08-19 18:56

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0033_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B-', 'B-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('O-', 'O-'), ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 56, 30, 245562)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('76285433-83eb-46f9-95cd-d19ab8e7ebe5'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Platelets', 'Platelets'), ('Blood', 'Blood'), ('Plasma', 'Plasma'), ('Power Red', 'Power Red')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('B-', 'B-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('O-', 'O-'), ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Bungoma', 'Bungoma'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kitui', 'Kitui'), ('Kiambu', 'Kiambu'), ('Laikipia', 'Laikipia'), ('Kericho', 'Kericho'), ('Kajiado', 'Kajiado'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Embu', 'Embu'), ('Nyamira', 'Nyamira'), ('Nyeri', 'Nyeri'), ('Trans Nzoia', 'Trans Nzoia'), ('Meru', 'Meru'), ('Kisii', 'Kisii'), ("Murang'a", "Murang'a"), ('Samburu', 'Samburu'), ('Nandi', 'Nandi'), ('Kwale', 'Kwale'), ('Garissa', 'Garissa'), ('Migori', 'Migori'), ('Tana River', 'Tana River'), ('West Pokot', 'West Pokot'), ('Lamu', 'Lamu'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kirinyaga', 'Kirinyaga'), ('Uasin Gishu', 'Uasin Gishu'), ('Nyandarua', 'Nyandarua'), ('Kakamega', 'Kakamega'), ('Kilifi', 'Kilifi'), ('Machakos', 'Machakos'), ('Isiolo', 'Homa Bay'), ('Wajir', 'Wajir'), ('Taita-Taveta', 'Taita-Taveta'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Homa Bay', 'Homa Bay'), ('Vihiga', 'Vihiga'), ('Makueni', 'Makueni'), ('Baringo', 'Baringo'), ('Nairobi', 'Nairobi'), ('Narok', 'Narok'), ('Bomet', 'Bomet'), ('Nakuru', 'Nakuru'), ('Turkana', 'Turkana')], default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 56, 30, 238570)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('a9e8c9f4-69e7-4788-b38e-d31fd7b007ea'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B-', 'B-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('O-', 'O-'), ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 56, 30, 248563)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 56, 30, 241567)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('33e0e0e6-b4b6-40b8-9306-6153a10f064a'), max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
    ]