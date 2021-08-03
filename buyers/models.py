from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_singnal = models.BooleanField(default=True)

    def __str__(self):
        return self.user


class Test(models.Model):
    name = models.CharField(max_length=10, blank=True)
    from_singnal = models.BooleanField(default=False)

    def __str__(self):
        return self.name
