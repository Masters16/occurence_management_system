# Generated by Django 3.0.5 on 2023-07-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_auto_20230715_1224'),
        ('blood', '0011_auto_20230714_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='blooddrives',
            name='volunteers',
            field=models.ManyToManyField(related_name='blood_drive', to='appointments.VolunteerRegistration'),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Kakamega', 'Kakamega'), ('Tana River', 'Tana River'), ('Busia', 'Busia'), ('Machakos', 'Machakos'), ('Narok', 'Narok'), ('Samburu', 'Samburu'), ('Nyamira', 'Nyamira'), ('Makueni', 'Makueni'), ('Uasin Gishu', 'Uasin Gishu'), ('Nakuru', 'Nakuru'), ('Kwale', 'Kwale'), ('Turkana', 'Turkana'), ('Kiambu', 'Kiambu'), ('Taita-Taveta', 'Taita-Taveta'), ('Nandi', 'Nandi'), ('Nairobi', 'Nairobi'), ('Baringo', 'Baringo'), ('Vihiga', 'Vihiga'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Meru', 'Meru'), ('Wajir', 'Wajir'), ("Murang'a", 'Murang'), ('Bungoma', 'Bungoma'), ('Bomet', 'Bomet'), ('Garissa', 'Garissa'), ('Embu', 'Embu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Homa Bay', 'Homa Bay'), ('Trans Nzoia', 'Trans Nzoia'), ('Nyandarua', 'Nyandarua'), ('Siaya', 'Siaya'), ('Kisii', 'Kisii'), ('Mandera', 'Mandera'), ('Mombasa', 'Mombasa'), ('Nyeri', 'Nyeri'), ('Kilifi', 'Kilifi'), ('Kitui', 'Kitui'), ('Kajiado', 'Kajiado'), ('Laikipia', 'Laikipia'), ('Isiolo', 'Homa Bay'), ('Kisumu', 'Kisumu'), ('Lamu', 'Lamu'), ('Kericho', 'Kericho'), ('Migori', 'Migori')], max_length=15),
        ),
    ]
