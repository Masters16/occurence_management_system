# Generated by Django 3.0.5 on 2023-07-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_auto_20230715_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('B-', 'B-'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
    ]
