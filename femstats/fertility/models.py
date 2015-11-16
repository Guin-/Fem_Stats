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
        (LIGHT, 'Light')
        (MEDIUM, 'Medium'),
        (HEAVY, 'Heavy'),
    )
    user = models.ForeignKey(User)
    date = models.DateField('Date')
    flow = models.Charfield(choices=FLOW_CHOICES,
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

class cervical(models.model):
    pass
'''
    user = models.foreignkey(user)
    date = models.datefield('date')
    fluid = models.charfield(choices=fluid_choices,
                                      default=none)
    position = models.charfield(choices=position_choices,
                                default=high)
    texture = models.charfield(choices=texture_choices,
                               default=firm)
    opening = models.charfield(choices=opening_choices,
                               default=open)

'''
