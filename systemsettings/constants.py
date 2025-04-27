from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class DurationChoices(TextChoices):
    ONE_DAY = 'one_day', _('1 day')
    ONE_WEEK = 'one_week', _('1 week')
    TWO_WEEKS = 'two_weeks', _('2 weeks')
    ONE_MONTH = 'one_month', _('1 month')
    THREE_MONTHS = 'three_months', _('3 months')
    SIX_MONTHS = 'six_months', _('6 months')
    ONE_YEAR = 'one_year', _('1 Year')
