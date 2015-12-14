from django.forms import ModelForm
from femstats.fertility.models import Period, BasalBodyTemp, Cervical

from betterforms.multiform import MultiModelForm

class PeriodForm(ModelForm):
    class Meta:
        model = Period
        fields = ['date', 'flow']

class BasalBodyTempForm(ModelForm):
    class Meta:
        model = BasalBodyTemp
        fields = ['date', 'time', 'temperature', 'scale']

class CervicalForm(ModelForm):
    class Meta:
        model = Cervical
        fields = ['date', 'mucus', 'position', 'texture', 'opening']

class FertilityMultiForm(MultiModelForm):
    form_classes = {
        'BasalBodyTemp': BasalBodyTempForm,
        'Cervical': CervicalForm,
    }
