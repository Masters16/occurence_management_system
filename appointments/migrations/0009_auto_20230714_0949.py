# Generated by Django 3.0.5 on 2023-07-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_auto_20230714_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Wajir', 'Wajir'), ('Nyandarua', 'Nyandarua'), ('Uasin Gishu', 'Uasin Gishu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('West Pokot', 'West Pokot'), ('Tana River', 'Tana River'), ('Vihiga', 'Vihiga'), ('Isiolo', 'Homa Bay'), ('Kiambu', 'Kiambu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Turkana', 'Turkana'), ('Kajiado', 'Kajiado'), ('Taita-Taveta', 'Taita-Taveta'), ('Homa Bay', 'Homa Bay'), ('Kwale', 'Kwale'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Nyeri', 'Nyeri'), ('Kisii', 'Kisii'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Makueni', 'Makueni'), ('Machakos', 'Machakos'), ('Busia', 'Busia'), ('Kakamega', 'Kakamega'), ('Kilifi', 'Kilifi'), ('Trans Nzoia', 'Trans Nzoia'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Nairobi', 'Nairobi'), ('Bomet', 'Bomet'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Garissa', 'Garissa'), ("Murang'a", 'Murang'), ('Kericho', 'Kericho'), ('Baringo', 'Baringo'), ('Nyamira', 'Nyamira'), ('Embu', 'Embu'), ('Nandi', 'Nandi'), ('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Mandera', 'Mandera'), ('Migori', 'Migori')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Wajir', 'Wajir'), ('Nyandarua', 'Nyandarua'), ('Uasin Gishu', 'Uasin Gishu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('West Pokot', 'West Pokot'), ('Tana River', 'Tana River'), ('Vihiga', 'Vihiga'), ('Isiolo', 'Homa Bay'), ('Kiambu', 'Kiambu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Turkana', 'Turkana'), ('Kajiado', 'Kajiado'), ('Taita-Taveta', 'Taita-Taveta'), ('Homa Bay', 'Homa Bay'), ('Kwale', 'Kwale'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Nyeri', 'Nyeri'), ('Kisii', 'Kisii'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Makueni', 'Makueni'), ('Machakos', 'Machakos'), ('Busia', 'Busia'), ('Kakamega', 'Kakamega'), ('Kilifi', 'Kilifi'), ('Trans Nzoia', 'Trans Nzoia'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Nairobi', 'Nairobi'), ('Bomet', 'Bomet'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Garissa', 'Garissa'), ("Murang'a", 'Murang'), ('Kericho', 'Kericho'), ('Baringo', 'Baringo'), ('Nyamira', 'Nyamira'), ('Embu', 'Embu'), ('Nandi', 'Nandi'), ('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Mandera', 'Mandera'), ('Migori', 'Migori')], max_length=100),
        ),
    ]
