import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class UserRegistration(models.Model):

    user_no = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4())
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/Police/', default="profile/Police/default.png", null=True,
                                    blank=True)
    name = models.CharField(max_length=20, null=False, default='Name')
    mobile = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(default="test@test.com")
    id_card = models.PositiveIntegerField(unique=True, null=False)
    created_date = models.DateTimeField(auto_now_add=False, default=timezone.datetime.now())

    def __str__(self):
        return f'{self.user_no} - {self.name}'

    def json(self):
        return {
            'user_no': self.user_no,
            'user': f'{self.user}',
            'name': self.name,
            'mobile': self.mobile,
            'email': self.email,
            'id_card': self.id_card,
            'created_date': self.created_date
        }