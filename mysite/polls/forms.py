from django import forms

class AthleteNameForm(forms.Form):
    athleteName = forms.CharField(label='Search for athlete', max_length=100)
