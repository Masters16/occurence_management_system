import uuid
import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from user import models as u_models


class Station(models.Model):
    station_id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4())
    station_name = models.CharField(max_length=50)

    def __str__(self):
        return self.station_name


# Create your models here.
class PoliceRegistration(models.Model):
    current_time = datetime.datetime.now()

    police_id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4())
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Police/', default="profile/Police/default.png", null=True,
                                    blank=True)
    mobile = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(default="test@test.com")
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=False, default=timezone.datetime.now())

    def __str__(self):
        return self.police_id


class OccurenceRecords(models.Model):
    current_time = datetime.datetime.now()

    record_id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4())
    police = models.ForeignKey(PoliceRegistration, on_delete=models.CASCADE)
    station_id = models.CharField(max_length=50, null=True, default="x")
    user_id = models.ForeignKey(u_models.UserRegistration, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=40)
    status = models.CharField(max_length=8, default="Pending",
                              choices={('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')})
    created_date = models.DateTimeField(auto_now_add=False, default=timezone.datetime.now())

    def __str__(self):
        return self.record_id

    def json(self):
        return {
            'record_id': self.record_id,
            'the_police': f'{self.police.police_id}',
            'station_id': self.station_id,
            'user_id': self.user_id,
            'description': self.description,
            'address': self.address,
            'status': self.status,
            'created_date': self.created_date
        }


class OccurenceReport(models.Model):
    police = models.ForeignKey(PoliceRegistration, on_delete=models.CASCADE)
    report_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4())
    station_id = models.CharField(max_length=50, null=True, default="x")
    title = models.CharField(max_length=100, default='Occurence-report')
    file = models.FileField(upload_to='reports/occurence-reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.report_id


class UserReport(models.Model):
    police = models.ForeignKey(PoliceRegistration, on_delete=models.CASCADE)
    report_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4())
    station_id = models.CharField(max_length=50, null=True, default="x")
    title = models.CharField(max_length=100, default='Donation-report')
    file = models.FileField(upload_to='reports/user-reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.report_id
