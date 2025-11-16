from django.db.models.signals import (
    post_save,
    post_delete
)
from django.dispatch import receiver
from . import models

''''
    TODO MAKE A SIGNALS FOR CREATING ACTIVE RENT
    INTEGRATE A MONEY LOGIC...

'''
@receiver(post_save, sender=models.RentHistory)
def ActiveRentSignals(sender, instance, created, **kwargs ):
    if created:
        models.ActiveRent.objects.create(
            rent_transaction=instance,
            room=instance.room,
            tenant=instance.renter,
            amount=instance.renter.budget,
        )
        
        room_instance = models.Room.objects.filter(room_id=instance.room.room_id).last()
        if room_instance.room_availability == 'Available':
            room_instance.room_availability = 'Not Available'
            room_instance.save()