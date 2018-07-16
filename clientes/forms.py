from django.forms import ModelForm
from django import forms
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

class SmsForm(forms.Form):
    telefone = forms.CharField(label='Telefone', max_length=15, initial="+5511")
    mensagem = forms.CharField(label='Mensagem', max_length=160,widget=forms.Textarea())
