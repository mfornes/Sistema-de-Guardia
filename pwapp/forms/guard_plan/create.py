from django.forms import ModelForm, DateInput
from pwapp.models import GuardPlan

class DateTimePickerInput(DateInput):
        input_type = 'date'

class CreateGuardPlanForm(ModelForm):  

    class Meta:
        model = GuardPlan
        fields = ('date', 'local',)
        widgets = {
            'date' : DateTimePickerInput(),
        }
