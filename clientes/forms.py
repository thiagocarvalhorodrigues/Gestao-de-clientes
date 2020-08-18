from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'Last_name', 'salary', 'Historia', 'Idade', 'photo']