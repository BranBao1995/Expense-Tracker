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