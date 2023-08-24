# Generated by Django 3.0.5 on 2023-07-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_auto_20230715_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('AB-', 'AB-'), ('A+', 'A+'), ('O-', 'O-'), ('B-', 'B-'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A', 'A')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=8),
        ),
    ]
