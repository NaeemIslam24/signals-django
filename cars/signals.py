from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import Car, Car_test
import uuid
from buyers.models import Buyer


@receiver(pre_save, sender=Car)
def pre_save_signal(sender, instance, **kwargs):

    if instance.test == "":
        instance.test = str(uuid.uuid4())[0:6]


@receiver(pre_save, sender=Car_test)
def pre_save_signal(sender, instance, **kwargs):

    obj = Buyer.objects.get(name=instance.name.name)
    print('--------------------------------')
    print(obj)
