# Generated by Django 4.2.3 on 2023-07-24 06:12

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0039_alter_blooddrives_county_alter_blooddrives_drive_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Embu', 'Embu'), ('Siaya', 'Siaya'), ('Kirinyaga', 'Kirinyaga'), ('Garissa', 'Garissa'), ('Machakos', 'Machakos'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Uasin Gishu', 'Uasin Gishu'), ('Narok', 'Narok'), ('Taita-Taveta', 'Taita-Taveta'), ('Nyeri', 'Nyeri'), ('Tana River', 'Tana River'), ('Meru', 'Meru'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Wajir', 'Wajir'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kitui', 'Kitui'), ('Makueni', 'Makueni'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('Samburu', 'Samburu'), ('Bungoma', 'Bungoma'), ('Bomet', 'Bomet'), ("Murang'a", "Murang'a"), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Kajiado', 'Kajiado'), ('Nyandarua', 'Nyandarua'), ('Mombasa', 'Mombasa'), ('Lamu', 'Lamu'), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Isiolo', 'Homa Bay'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Baringo', 'Baringo'), ('Migori', 'Migori'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Busia', 'Busia')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('c380af1e-a2ad-451e-8220-2bb1922e41db'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('A', 'A'), ('B+', 'B+'), ('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 9, 12, 23, 384932)),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
    ]
