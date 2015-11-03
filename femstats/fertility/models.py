from django.db import models

# Create your models here.

class Period(models.Model):
    pass

class BasalBodyTemperature(models.Model):
    FAHRENHEIT = 'F'
    CELSIUS = 'C'
    TEMPERATURE_SCALE_CHOICES = (
        (FAHRENHEIT, 'Fahrenheit'),
        (CELSIUS, 'Celsius'),
    )
    temperature = models.PositiveSmallIntegerField()
    scale = models.CharField(max_length=1,
                             choices=TEMPERATURE_SCALE_CHOICES,
                             default=FAHRENHEIT)

class Cervical(models.Model):
    pass
