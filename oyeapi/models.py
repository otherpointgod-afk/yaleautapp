from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER = (
    ('Male', 'Male')
    ('Female', 'Female')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="default", default='https://example.com/default-profile-pic.png',null = True , blank = True)

    def _str_(self):
        return self.fullname
