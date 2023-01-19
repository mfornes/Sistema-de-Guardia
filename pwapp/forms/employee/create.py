from django.forms import ModelForm, DateInput
from pwapp.models import Employee

class DateTimePickerInput(DateInput):
        input_type = 'date'
        

class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('area', 'recidence', 'sexo', 'name', 'last_name',)
        widgets = {
            'date' : DateTimePickerInput(),
        }

    def clean(self):

        super(CreateEmployeeForm, self).clean()

        name = self.cleaned_data.get('name').replace(" ", "")
        last_name = self.cleaned_data.get('last_name').replace(" ", "")

        if not str(name).isalpha():
            self._errors['name'] = self.error_class(['Solo letras'])
        if not str(last_name).isalpha():
            self._errors['last_name'] = self.error_class(['Solo letras'])
        return self.cleaned_data