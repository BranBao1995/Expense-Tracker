from django import forms
from django.forms import ModelForm
from .models import Expense
import datetime

max_year = datetime.datetime.now().year


years = []

for year in range(max_year, 1899, -1):
    years.append(str(year))

# Django form field cannot use 'validators=[]' argument, instead, specify max_length, min_length, max_value, min_value
# or refer to https://docs.djangoproject.com/en/4.1/ref/forms/fields/ instead

class AddForm(ModelForm):
     class Meta:
        model = Expense
       
        fields = "__all__"

        labels = {
            'title':"Title",
            'date':"Date",
            'amount':'Amount',
            'description': 'Description'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'edit_title'}),
            'date': forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns'}),
            'amount': forms.NumberInput(attrs={'class': 'edit_amount'}),
            'description': forms.Textarea(attrs={'class': 'edit_description'})
        }

        error_messages = {
            'title': {
                'min_length': 'Yo! Minimum length must be 5',
                'max_length': 'Yo! Maximum length is 100'
            },
            'amount':{
                'min_value': "Yo! Minimum value must be 0",
            }
        }


class EditForm(ModelForm):
     class Meta:
        model = Expense
       
        fields = "__all__"

        labels = {
            'title':"Title",
            'date':"Date",
            'amount':'Amount',
            'description': 'Description'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'edit_title'}),
            'date': forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns'}),
            'amount': forms.NumberInput(attrs={'class': 'edit_amount'}),
            'description': forms.Textarea(attrs={'class': 'edit_description'})
        }

        error_messages = {
            'title': {
                'min_length': 'Yo! Minimum length must be 5',
                'max_length': 'Yo! Maximum length is 100'
            },
            'amount':{
                'min_value': "Yo! Minimum value must be 0",
            }
        }



class DateForm(forms.Form):
    date = forms.DateField(label='Select a date', widget=forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns'}))

# class EditForm(forms.Form):
#     title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'edit_title'}), min_length=1, max_length=100)
#     date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns edit_date'}))
#     amount = forms.IntegerField(label='Dollar Amount', widget=forms.NumberInput(attrs={'class': 'edit_amount'}), min_value=0)
#     description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'edit_description'}))

# class AddForm(forms.Form):
#     title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'edit_title'}), min_length=1, max_length=100)
#     date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns edit_date'}))
#     amount = forms.IntegerField(label='Dollar Amount', widget=forms.NumberInput(attrs={'class': 'edit_amount'}), min_value=0)
#     description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'edit_description'}))

