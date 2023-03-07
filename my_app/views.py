from django.shortcuts import render
from django.http.response import HttpResponse
from . import models
from .forms import DateForm
import datetime

# Create your views here.

def landing(request):
    return render(request, 'my_app/landing.html')

def main(request):
    form = DateForm()
    if (request.GET):
        data = request.GET
        year = data['date_year']

        if int(data['date_month']) < 10:
            month = '0' + data['date_month']
        else:
            month = data['date_month']

        if int(data['date_day']) < 10:
            day = '0' + data['date_day']
        else:
            day = data['date_day']

        date = year + '-' + month + '-' + day
        all_expenses = models.Expense.objects.filter(date=date)
    else:
        all_expenses = models.Expense.objects.all()
    
    context = {'expenses': all_expenses, 'form': form}
    return render(request,'my_app/main.html',context=context)      
    


def edit(request):
    return render(request, 'my_app/edit.html')
