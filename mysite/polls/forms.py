from django import forms

class AthleteNameForm(forms.Form):
    athletename = forms.CharField(label='Search for athlete', max_length=100)
