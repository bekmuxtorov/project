from django.db.models.signals import pre_save
from django.dispatch import receiver

from karer.models import Order
from tax_officer.models import Violation


@receiver(pre_save, sender=Order)
@receiver(pre_save, sender=Violation)
def delete_file_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_file = sender.objects.get(pk=instance.pk).car_photo
        except sender.DoesNotExist:
            return
        new_file = instance.car_photo
        if not old_file == new_file:
            old_file.delete(save=False)
