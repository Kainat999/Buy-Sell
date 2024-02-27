from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    SELLER = 'seller'
    USER_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller'),
    ]
    
    role = models.CharField(max_length=20, choices=USER_CHOICES)
    email_verified = models.BooleanField(default=False)

    email = models.EmailField(unique=True)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']  
    def __str__(self):
        return self.email
