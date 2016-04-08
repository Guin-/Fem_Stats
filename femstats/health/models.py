from django.db import models
from django.core.urlresolvers import reverse

import datetime

from femstats.users.models import User

class Health(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    STRESS_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    MINUTESa = 'less than 30'
    MINUTESb = 'half hour to hour'
    MINUTESc = '60+'

    EXERCISE_CHOICES = (
        (MINUTESa, '<30'),
        (MINUTESb, '30-60'),
        (MINUTESc, '60+'),
    )

    user = models.ForeignKey(User)
    date = models.DateField('Date', default=datetime.date.today)
    sleep = models.PositiveSmallIntegerField(null=True, blank=True)
    alcohol_intake = models.PositiveSmallIntegerField(null=True, blank=True)
    exercise = models.CharField(max_length=10, choices=EXERCISE_CHOICES, blank=True)
    stress_level = models.CharField(max_length=6,
                                    choices=STRESS_CHOICES, blank=True)

    def __unicode__(self):
        return self.user

    def get_absolute_url(self):
        pass
