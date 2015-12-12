from django.forms import ModelForm
from femstats.fertility.models import Period

class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = ['date', 'flow']

