# Generated by Django 3.0.5 on 2023-07-15 20:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0017_auto_20230715_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonate',
            name='id',
        ),
        migrations.AddField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('e0a9b411-589f-4605-b137-62c9dff84076'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Donor'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A+', 'A+'), ('O-', 'O-'), ('AB-', 'AB-'), ('A', 'A'), ('B-', 'B-')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('7d5d7f90-79ed-486b-8fa1-e595d47359e6'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
    ]
