from django import forms

class Competition(forms.Form):
    name =  forms.ChoiceField(choices=())