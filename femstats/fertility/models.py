from django.db import models
from femstats.users.models import User

# Create your models here.

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
    user = models.ForeignKey(User)
    date = models.DateField('Date')
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
    user = models.ForeignKey(User)
    date = models.DateField('Date')
    time = models.TimeField('Time')
    temperature = models.PositiveSmallIntegerField()
    scale = models.CharField(max_length=1,
                             choices=TEMPERATURE_SCALE_CHOICES,
                             default=FAHRENHEIT)

    def __unicode__(self):
        return self.temperature

class cervical(models.Model):
    pass
'''
    user = models.ForeignKey(user)
    date = models.DateField('date')
    fluid = models.CharField(choices=fluid_choices,
                                      default=none)
    position = models.CharField(choices=position_choices,
                                default=high)
    texture = models.CharField(choices=texture_choices,
                               default=firm)
    opening = models.CharField(choices=opening_choices,
                               default=open)

'''
