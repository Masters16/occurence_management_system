# Generated by Django 4.2.3 on 2023-08-23 15:29

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0047_alter_blooddrives_county_alter_blooddrives_drive_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Vihiga', 'Vihiga'), ('Kirinyaga', 'Kirinyaga'), ('Bungoma', 'Bungoma'), ("Murang'a", "Murang'a"), ('Busia', 'Busia'), ('Turkana', 'Turkana'), ('Machakos', 'Machakos'), ('Kitui', 'Kitui'), ('Mombasa', 'Mombasa'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Garissa', 'Garissa'), ('Kiambu', 'Kiambu'), ('Migori', 'Migori'), ('Bomet', 'Bomet'), ('Homa Bay', 'Homa Bay'), ('Nyandarua', 'Nyandarua'), ('Nairobi', 'Nairobi'), ('Siaya', 'Siaya'), ('Nyamira', 'Nyamira'), ('West Pokot', 'West Pokot'), ('Tana River', 'Tana River'), ('Laikipia', 'Laikipia'), ('Meru', 'Meru'), ('Isiolo', 'Homa Bay'), ('Lamu', 'Lamu'), ('Kilifi', 'Kilifi'), ('Kericho', 'Kericho'), ('Kakamega', 'Kakamega'), ('Wajir', 'Wajir'), ('Nakuru', 'Nakuru'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Taita-Taveta', 'Taita-Taveta'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Makueni', 'Makueni'), ('Kisumu', 'Kisumu'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Kajiado', 'Kajiado'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Embu', 'Embu'), ('Baringo', 'Baringo'), ('Samburu', 'Samburu'), ('Nyeri', 'Nyeri')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('fb8ffaec-fd8a-44bd-b8a7-4994865638b9'), max_length=60, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('B-', 'B-'), ('O-', 'O-'), ('A+', 'A+'), ('A', 'A'), ('AB-', 'AB-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 18, 29, 6, 3847)),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
