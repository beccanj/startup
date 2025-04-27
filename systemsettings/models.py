from django.db import models
from base.models import BaseModel
from systemsettings.constants import DurationChoices


class SystemSettings(BaseModel):
    enable_subscription_expiry = models.BooleanField(default=False)
    subscription_duration = models.CharField(max_length=100, choices=DurationChoices.choices, null=True)
