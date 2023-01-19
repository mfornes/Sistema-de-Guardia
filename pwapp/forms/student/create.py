from django.forms import ModelForm, DateInput
from pwapp.models import Student

class DateTimePickerInput(DateInput):
        input_type = 'date'

class CreateStudentForm(ModelForm):  
    class Meta:
        model = Student
        fields = ('careers', 'anno', 'group', 'sexo', 'name', 'last_name',)
        widgets = {
            'date' : DateTimePickerInput(),
        }
    
    def clean(self):

        super(CreateStudentForm, self).clean()

        name = self.cleaned_data.get('name').replace(" ", "")
        last_name = self.cleaned_data.get('last_name').replace(" ", "")
        group = self.cleaned_data.get('group')

        if not str(name).isalpha():
            self._errors['name'] = self.error_class(['Solo letras'])
        if not str(last_name).isalpha():
            self._errors['last_name'] = self.error_class(['Solo letras'])
        if not str(group).isnumeric():
            self._errors['group'] = self.error_class(['Solo números'])

        return self.cleaned_data