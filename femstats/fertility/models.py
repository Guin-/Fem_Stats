from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime

from femstats.users.models import User

class Period(models.Model):
    SPOTTING ='Spotting'
    LIGHT = 'Light'
    MEDIUM = 'Medium'
    HEAVY = 'Heavy'
    FLOW_CHOICES = (
        (SPOTTING, 'Spotting'),
        (LIGHT, 'Light'),
        (MEDIUM, 'Medium'),
        (HEAVY, 'Heavy'),
    )
    user = models.ForeignKey(User)
    date = models.DateField('Date', default=datetime.date.today)
    flow = models.CharField(max_length=10,
                            choices=FLOW_CHOICES)

    def __unicode__(self):
        return self.flow

    def get_absolute_url(self):
        return reverse('fertility:period', kwargs={'pk': self.pk})

class Fertility(models.Model):
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    TEMPERATURE_SCALE_CHOICES = (
        (FAHRENHEIT, 'Fahrenheit'),
        (CELSIUS, 'Celsius'),
    )

    DRY = 'Dry'
    STICKY = 'Sticky'
    CREAMY = 'Creamy'
    WATERY = 'Watery'
    EGG_WHITE = 'Egg White'

    MUCUS_CHOICES = (
        (DRY, 'Dry'),
        (STICKY, 'Sticky'),
        (CREAMY, 'Creamy'),
        (WATERY, 'Watery'),
        (EGG_WHITE, 'Egg White'),
    )

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    POSITION_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    SOFT = 'Soft'
    FIRM = 'Firm'

    TEXTURE_CHOICES = (
        (SOFT,'Soft'),
        (MEDIUM, 'Medium'),
        (FIRM, 'Firm'),
    )

    OPEN = 'Open'
    CLOSED = 'Closed'

    OPENING_CHOICES = (
        (OPEN, 'Open'),
        (MEDIUM, 'Medium'),
        (CLOSED, 'Closed'),
    )

    user = models.ForeignKey(User)
    date = models.DateField('Date', default=datetime.date.today)
    time = models.TimeField('Time', default=timezone.now)
    temperature = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=True, blank=True)
    scale = models.CharField(max_length=1,
                             choices=TEMPERATURE_SCALE_CHOICES, blank=True)
    mucus = models.CharField(max_length=10,
                             choices=MUCUS_CHOICES, blank=True)
    position = models.CharField(max_length=10,
                                choices=POSITION_CHOICES, blank=True)
    texture = models.CharField(max_length=10,
                               choices=TEXTURE_CHOICES, blank=True)
    opening = models.CharField(max_length=10,
                               choices=OPENING_CHOICES, blank=True)

    def __unicode__(self):
        return self.position


    def get_absolute_url(self):
        return reverse('fertility:fertility', kwargs={'pk': self.pk})

