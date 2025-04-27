from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class CategoryType(TextChoices):
    CROP = 'crop', _('Crop')
    LIVESTOCK = 'livestock', _('Livestock')


class SoilTestStatus(TextChoices):
    PENDING = 'pending', _('Pending')
    PAID = 'paid', _('Paid')
    FAILED = 'failed', _('Failed')
    SUCCESSFUL = 'successful', _('Successful')


class SubscriptionStatus(TextChoices):
    PENDING = 'pending', _('Pending')
    FAILED = 'failed', _('Failed')
    SUCCESSFUL = 'successful', _('Successful')
    CANCELLED = 'cancelled', _('Cancelled')
