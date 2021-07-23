from django.db.models.signals import pre_save
from django.dispatch import receiver
from . models import Car
import uuid


@receiver(pre_save, sender=Car)
def pre_save_signal(sender, instance, **kwargs):

    if instance.test == "":
        instance.test = str(uuid.uuid4())[0:6]
