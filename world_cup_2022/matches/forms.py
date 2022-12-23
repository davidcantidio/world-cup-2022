from django import forms
from .models import Competition

class CompetitionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CompetitionForm, self).__init__(*args, **kwargs)

        choices = [(competition.id, competition.name) 
                for competition in Competition.objects.all()]

        self.fields['competitions'] = forms.ChoiceField(choices=choices)
