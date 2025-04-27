from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from farming.constants import SubscriptionStatus


class Service(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ServiceProvider(BaseModel):
    services = models.ManyToManyField(Service, related_name='providers')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='service_provider')
    location_name = models.CharField(max_length=100)
    location_address = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    location_pin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.business_name


class ServiceSubscription(BaseModel):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.PROTECT, related_name='subscriptions')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    additional_cost = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='subscriptions')
    status = models.CharField(max_length=100, choices=SubscriptionStatus.choices)
