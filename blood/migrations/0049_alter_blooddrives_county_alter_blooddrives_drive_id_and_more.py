# Generated by Django 4.2.3 on 2023-08-23 17:42

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0048_alter_blooddrives_county_alter_blooddrives_drive_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Siaya', 'Siaya'), ('Nyamira', 'Nyamira'), ('Garissa', 'Garissa'), ('Mombasa', 'Mombasa'), ('Migori', 'Migori'), ('Isiolo', 'Homa Bay'), ('Bomet', 'Bomet'), ('Nandi', 'Nandi'), ('Kiambu', 'Kiambu'), ('Vihiga', 'Vihiga'), ('Nyandarua', 'Nyandarua'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Kilifi', 'Kilifi'), ('Samburu', 'Samburu'), ('Taita-Taveta', 'Taita-Taveta'), ('Embu', 'Embu'), ('Trans Nzoia', 'Trans Nzoia'), ('Laikipia', 'Laikipia'), ('Kwale', 'Kwale'), ('Homa Bay', 'Homa Bay'), ('West Pokot', 'West Pokot'), ('Busia', 'Busia'), ('Makueni', 'Makueni'), ('Kitui', 'Kitui'), ('Kisii', 'Kisii'), ("Murang'a", "Murang'a"), ('Mandera', 'Mandera'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nyeri', 'Nyeri'), ('Wajir', 'Wajir'), ('Kericho', 'Kericho'), ('Baringo', 'Baringo'), ('Machakos', 'Machakos'), ('Kakamega', 'Kakamega'), ('Turkana', 'Turkana'), ('Kirinyaga', 'Kirinyaga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Uasin Gishu', 'Uasin Gishu'), ('Nairobi', 'Nairobi'), ('Bungoma', 'Bungoma'), ('Meru', 'Meru'), ('Marsabit', 'Marsabit'), ('Narok', 'Narok'), ('Nakuru', 'Nakuru')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('8ce45013-8327-4117-8e15-a537074bba3a'), max_length=60, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('A', 'A'), ('O-', 'O-'), ('AB+', 'AB+'), ('O+', 'O+'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 935691)),
        ),
    ]
