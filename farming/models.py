from base.models import BaseModel
from farming.constants import CategoryType, SoilTestStatus, SubscriptionStatus
from django.contrib.auth.models import User
from django.db import models


class Category(BaseModel):
    name = models.CharField(max_length=200)
    category_type = models.CharField(max_length=50, choices=CategoryType.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Practice(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='practices')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    list_of_stages = models.JSONField(default=list)
    soil_test_valid_duration = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('category', 'name')


class Farm(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farms')
    coordinate_1 = models.CharField(max_length=100)
    coordinate_2 = models.CharField(max_length=100)
    coordinate_3 = models.CharField(max_length=100)
    coordinate_4 = models.CharField(max_length=100)


class UserPractice(BaseModel):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='user_practices')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_practices')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class SoilTest(BaseModel):
    user_practice = models.ForeignKey(UserPractice, on_delete=models.CASCADE, related_name='tests')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='tests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    document = models.FileField(upload_to='soil_tests/', null=True, blank=True)
    next_soil_test = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=SoilTestStatus.choices)


class Subscription(BaseModel):
    soil_test = models.ForeignKey(SoilTest, on_delete=models.SET_NULL, null=True, blank=True, related_name='tests')
    blog = models.ForeignKey('main.Article', on_delete=models.SET_NULL, null=True, blank=True, related_name='subscriptions')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=SubscriptionStatus.choices)
