from django import forms

class DateForm(forms.Form):
    date = forms.DateField(label='Select a date', required=True)