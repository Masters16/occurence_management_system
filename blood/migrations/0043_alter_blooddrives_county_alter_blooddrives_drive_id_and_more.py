# Generated by Django 4.2.3 on 2023-07-24 11:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0042_alter_blooddrives_county_alter_blooddrives_drive_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Tana River', 'Tana River'), ('Kisii', 'Kisii'), ('Kitui', 'Kitui'), ('Uasin Gishu', 'Uasin Gishu'), ('Kisumu', 'Kisumu'), ('Kericho', 'Kericho'), ('Nandi', 'Nandi'), ('Kajiado', 'Kajiado'), ('Kilifi', 'Kilifi'), ('Marsabit', 'Marsabit'), ('Nyeri', 'Nyeri'), ('Siaya', 'Siaya'), ('Turkana', 'Turkana'), ('Samburu', 'Samburu'), ('Kwale', 'Kwale'), ('Nyandarua', 'Nyandarua'), ('Kakamega', 'Kakamega'), ('Migori', 'Migori'), ('Baringo', 'Baringo'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Makueni', 'Makueni'), ('Busia', 'Busia'), ('Bungoma', 'Bungoma'), ('Lamu', 'Lamu'), ("Murang'a", "Murang'a"), ('Nakuru', 'Nakuru'), ('Mandera', 'Mandera'), ('Laikipia', 'Laikipia'), ('West Pokot', 'West Pokot'), ('Trans Nzoia', 'Trans Nzoia'), ('Kirinyaga', 'Kirinyaga'), ('Isiolo', 'Homa Bay'), ('Meru', 'Meru'), ('Wajir', 'Wajir'), ('Homa Bay', 'Homa Bay'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Mombasa', 'Mombasa'), ('Narok', 'Narok'), ('Vihiga', 'Vihiga'), ('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('Kiambu', 'Kiambu'), ('Bomet', 'Bomet'), ('Garissa', 'Garissa'), ('Nyamira', 'Nyamira')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('84049f26-abca-43f7-9c27-1a09e602379a'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('B-', 'B-'), ('AB-', 'AB-'), ('B+', 'B+'), ('O-', 'O-'), ('A', 'A'), ('A+', 'A+'), ('O+', 'O+'), ('AB+', 'AB+')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 14, 28, 3, 410117)),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
    ]
