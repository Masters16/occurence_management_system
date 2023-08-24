# Generated by Django 3.0.5 on 2023-07-15 17:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0020_auto_20230715_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Wajir', 'Wajir'), ('Kakamega', 'Kakamega'), ('Kwale', 'Kwale'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kisumu', 'Kisumu'), ('Kiambu', 'Kiambu'), ('Embu', 'Embu'), ('Trans Nzoia', 'Trans Nzoia'), ('Nakuru', 'Nakuru'), ('Migori', 'Migori'), ('Isiolo', 'Homa Bay'), ('Kisii', 'Kisii'), ('Meru', 'Meru'), ('Nandi', 'Nandi'), ('Homa Bay', 'Homa Bay'), ('Makueni', 'Makueni'), ('Uasin Gishu', 'Uasin Gishu'), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Laikipia', 'Laikipia'), ('Siaya', 'Siaya'), ('Nyamira', 'Nyamira'), ('Garissa', 'Garissa'), ('Bomet', 'Bomet'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Busia', 'Busia'), ('Mombasa', 'Mombasa'), ('Vihiga', 'Vihiga'), ('West Pokot', 'West Pokot'), ('Mandera', 'Mandera'), ('Nyeri', 'Nyeri'), ('Taita-Taveta', 'Taita-Taveta'), ('Tana River', 'Tana River'), ('Bungoma', 'Bungoma'), ('Marsabit', 'Marsabit'), ('Kitui', 'Kitui'), ('Nairobi', 'Nairobi'), ('Kirinyaga', 'Kirinyaga'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Samburu', 'Samburu'), ('Nyandarua', 'Nyandarua'), ('Turkana', 'Turkana'), ('Lamu', 'Lamu'), ('Baringo', 'Baringo'), ('Machakos', 'Machakos'), ("Murang'a", 'Murang')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('7ee14862-a264-41da-91d2-cf9ef31e5915'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
