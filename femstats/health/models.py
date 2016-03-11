from django.db import models
from django.core.urlresolvers import reverse

import datetime

from femstats.users.models import User

class Physical(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField('Date', default=datetime.date.today)
    sleep = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.sleep

    def get_absolute_url(self):
        pass

class Mental(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField('Date', default=datetime.date.today)

    def __unicode__(self):
        return self.user

    def get_absolute_url(self):
        pass
