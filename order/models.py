from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()



class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserDetails(TimeStampedModel):
    user = models.ForeignKey(User, related_name="user_details", 
                            on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    address_line1 = models.CharField(max_length=250, blank=True, null=True)
    address_line2 = models.CharField(max_length=250, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    building = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = "User Details"
        verbose_name_plural = "User Details"



class Order(TimeStampedModel):
    PENDING = 'p'
    DELIVERED = 'd'

    ORDER_CHOICE = (
        (PENDING, "Pending"),
        (DELIVERED, "Delivered"),
    )

    pizza_number = models.IntegerField(default=0)
    pizza_size = models.CharField(max_length=250)
    status = models.CharField(max_length=1, choices=ORDER_CHOICE, default=PENDING)
    describe_order = models.TextField(blank=True, null=True)
    user_details = models.ForeignKey(UserDetails, related_name="order", 
                            on_delete=models.CASCADE)

    