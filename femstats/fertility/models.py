from django.db import models
from femstats.users.models import User
import datetime

class Period(models.Model):
    SPOTTING ='SP'
    LIGHT = 'L'
    MEDIUM = 'M'
    HEAVY = 'H'
    FLOW_CHOICES = (
        (SPOTTING, 'Spotting'),
        (LIGHT, 'Light'),
        (MEDIUM, 'Medium'),
        (HEAVY, 'Heavy'),
    )
    user = models.ForeignKey(User, null=True)
    date = models.DateField('Date', default=datetime.date.today)
    flow = models.CharField(max_length=10,
                            choices=FLOW_CHOICES,
                            default=SPOTTING)

    def __unicode__(self):
        return self.flow

class BasalBodyTemp(models.Model):
    FAHRENHEIT = 'F'
    CELSIUS = 'C'
    TEMPERATURE_SCALE_CHOICES = (
        (FAHRENHEIT, 'Fahrenheit'),
        (CELSIUS, 'Celsius'),
    )
    user = models.ForeignKey(User, null=True)
    date = models.DateField('Date', default=datetime.date.today)
    time = models.TimeField('Time')
    temperature = models.PositiveSmallIntegerField()
    scale = models.CharField(max_length=1,
                             choices=TEMPERATURE_SCALE_CHOICES,
                             default=FAHRENHEIT)

    def __unicode__(self):
        return self.temperature

class Cervical(models.Model):
    DRY = 'D'
    STICKY = 'S'
    CREAMY = 'C'
    WATERY = 'W'
    EGG_WHITE = 'EW'

    MUCUS_CHOICES = (
        (DRY, 'Dry'),
        (STICKY, 'Sticky'),
        (CREAMY, 'Creamy'),
        (WATERY, 'Watery'),
        (EGG_WHITE, 'Egg White'),
    )

    LOW = 'LW'
    MEDIUM = 'MD'
    HIGH = "HI"

    POSITION_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    SOFT = 'ST'
    FIRM = 'FM'

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
        (CLOSED, 'Closed')
    )
    user = models.ForeignKey(User, null=True)
    date = models.DateField('Date', default=datetime.date.today)
    mucus = models.CharField(max_length=10,
                             choices=MUCUS_CHOICES,
                             default=DRY)
    position = models.CharField(max_length=10,
                                choices=POSITION_CHOICES,
                                default=HIGH)
    texture = models.CharField(max_length=10,
                               choices=TEXTURE_CHOICES,
                               default=FIRM)
    opening = models.CharField(max_length=10,
                               choices=OPENING_CHOICES,
                               default=OPEN)

    def __unicode__(self):
        return self.position


