from django.forms import ModelForm
from femstats.fertility.models import Period, Fertility

class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = ['date', 'flow']

class FertilityForm(ModelForm):
    class Meta:
        model = Fertility
        fields = ['date', 'time', 'temperature', 'scale',
                  'mucus', 'position', 'texture', 'opening']

