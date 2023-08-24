# Generated by Django 3.0.5 on 2023-07-15 17:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0016_auto_20230715_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A', 'A'), ('O+', 'O+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('A+', 'A+'), ('AB+', 'AB+'), ('O-', 'O-')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('53234e83-5890-4e72-a708-67bc2d5c8d45'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
    ]
