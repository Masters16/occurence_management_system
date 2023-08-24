# Generated by Django 4.2.3 on 2023-08-23 17:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('user_no', models.CharField(default=uuid.UUID('f3c96e83-f491-4209-a453-d8b13822fbde'), max_length=40, primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, default='profile/Police/default.png', null=True, upload_to='profile_pic/Police/')),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(default='test@test.com', max_length=254)),
                ('id_card', models.PositiveIntegerField(unique=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2023, 8, 23, 20, 42, 41, 987660))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
