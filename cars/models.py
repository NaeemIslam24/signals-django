from django.db import models
from buyers.models import Buyer
import uuid

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    code = models.CharField(max_length=10, blank=True)
    test = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.name}-{self.price}'

    # object override start
    # here self.code is override with uuid genaraor.
    # self.test is override in signals.py
    def save(self, *args, **kwargs):

        if self.code == "":
            self.code = str(uuid.uuid4()).upper()[0:10]

        return super().save(*args, **kwargs)
    # object override end
