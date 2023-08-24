# Generated by Django 4.2.3 on 2023-07-20 09:01

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0027_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B+', 'B+'), ('O-', 'O-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('A+', 'A+'), ('B-', 'B-'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 12, 1, 19, 344298)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('eebf10da-ef5c-48b7-8973-c7457c469483'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Power Red', 'Power Red'), ('Platelets', 'Platelets'), ('Plasma', 'Plasma'), ('Blood', 'Blood')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('B+', 'B+'), ('O-', 'O-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('A+', 'A+'), ('B-', 'B-'), ('O+', 'O+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 12, 1, 19, 339299)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('44147127-6b6c-4f0e-882d-1bf9fadd7c08'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B+', 'B+'), ('O-', 'O-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('A', 'A'), ('A+', 'A+'), ('B-', 'B-'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Nil', 'Nil')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 12, 1, 19, 341298)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('f70e0b47-67c3-471a-b320-56d7cfcc6667'), max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
    ]
