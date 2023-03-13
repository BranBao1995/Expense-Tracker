from django import forms
import datetime

max_year = datetime.datetime.now().year

# print(max_year)

years = []

for year in range(max_year, 1899, -1):
    years.append(str(year))

# print(years)

class DateForm(forms.Form):
    date = forms.DateField(label='Select a date', required=True, widget=forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns'}))

class EditForm(forms.Form):
    title = forms.CharField(label='Title', required=True, widget=forms.TextInput(attrs={'class': 'edit_title'}))
    date = forms.DateField(label='Date', required=True, widget=forms.SelectDateWidget(years=years, attrs={'class': 'dropdowns edit_date'}))
    amount = forms.CharField(label='Dollar Amount', required=True, widget=forms.TextInput(attrs={'class': 'edit_amount'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'edit_description'}))