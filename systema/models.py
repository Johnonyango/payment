from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    customer_name = models.CharField(max_length = 200)
    # customer_number = models.phonenumber_field(null=False, blank=False, unique=True)