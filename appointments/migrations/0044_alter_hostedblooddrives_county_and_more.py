# Generated by Django 4.2.3 on 2023-07-24 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0043_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Nakuru', 'Nakuru'), ('Kwale', 'Kwale'), ('Nyamira', 'Nyamira'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nyandarua', 'Nyandarua'), ('Narok', 'Narok'), ('Baringo', 'Baringo'), ('Mombasa', 'Mombasa'), ('Siaya', 'Siaya'), ('Kiambu', 'Kiambu'), ('Meru', 'Meru'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Nyeri', 'Nyeri'), ('Makueni', 'Makueni'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Machakos', 'Machakos'), ('Turkana', 'Turkana'), ('Kitui', 'Kitui'), ('Kisii', 'Kisii'), ('Kakamega', 'Kakamega'), ('Kilifi', 'Kilifi'), ('Wajir', 'Wajir'), ('Laikipia', 'Laikipia'), ('Uasin Gishu', 'Uasin Gishu'), ('Homa Bay', 'Homa Bay'), ('Vihiga', 'Vihiga'), ('Busia', 'Busia'), ('Migori', 'Migori'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Lamu', 'Lamu'), ('Samburu', 'Samburu'), ("Murang'a", 'Murang'), ('Garissa', 'Garissa'), ('Mandera', 'Mandera'), ('Kericho', 'Kericho'), ('Trans Nzoia', 'Trans Nzoia'), ('Kirinyaga', 'Kirinyaga'), ('Tana River', 'Tana River'), ('Marsabit', 'Marsabit'), ('Nandi', 'Nandi'), ('Kajiado', 'Kajiado'), ('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Nakuru', 'Nakuru'), ('Kwale', 'Kwale'), ('Nyamira', 'Nyamira'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nyandarua', 'Nyandarua'), ('Narok', 'Narok'), ('Baringo', 'Baringo'), ('Mombasa', 'Mombasa'), ('Siaya', 'Siaya'), ('Kiambu', 'Kiambu'), ('Meru', 'Meru'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Nyeri', 'Nyeri'), ('Makueni', 'Makueni'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Machakos', 'Machakos'), ('Turkana', 'Turkana'), ('Kitui', 'Kitui'), ('Kisii', 'Kisii'), ('Kakamega', 'Kakamega'), ('Kilifi', 'Kilifi'), ('Wajir', 'Wajir'), ('Laikipia', 'Laikipia'), ('Uasin Gishu', 'Uasin Gishu'), ('Homa Bay', 'Homa Bay'), ('Vihiga', 'Vihiga'), ('Busia', 'Busia'), ('Migori', 'Migori'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Lamu', 'Lamu'), ('Samburu', 'Samburu'), ("Murang'a", 'Murang'), ('Garissa', 'Garissa'), ('Mandera', 'Mandera'), ('Kericho', 'Kericho'), ('Trans Nzoia', 'Trans Nzoia'), ('Kirinyaga', 'Kirinyaga'), ('Tana River', 'Tana River'), ('Marsabit', 'Marsabit'), ('Nandi', 'Nandi'), ('Kajiado', 'Kajiado'), ('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('d561cea7-aa45-4a98-ba69-219c46f6ea5b'), max_length=20, primary_key=True, serialize=False),
        ),
    ]