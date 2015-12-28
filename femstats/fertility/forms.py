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
        fields = ['mucus', 'position', 'texture', 'opening']

class FertilityMultiForm(MultiModelForm):
    form_classes = {
        'BasalBodyTemp': BasalBodyTempForm,
        'Cervical': CervicalForm,
    }

    def save(self, commit=True):
        objects = super(FertilityMultiForm, self).save(commit=False)

        if commit:
            BasalBodyTemp = objects['BasalBodyTemp']
            Cervical = objects['Cervical']
#            BasalBodyTemp.user = self.request.user
#            Cervical.user = self.request.user
            BasalBodyTemp.save()
            Cervical.save()

        return objects


