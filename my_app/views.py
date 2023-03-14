from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import DateForm, EditForm
import datetime

# Create your views here.

def landing(request):
    return render(request, 'my_app/landing.html')

def main(request):
    form = DateForm()
    if request.GET:
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
    


def edit(request, target):

    if request.method == 'POST':
        print(request.POST)
        form = EditForm(request.POST)

        if form.is_valid():
            expense = models.Expense.objects.get(pk=int(target))

            title = request.POST['title']
            amount = request.POST['amount']
            description = request.POST['description']
            year = request.POST['date_year']
            month = request.POST['date_month']
            day = request.POST['date_day']

            if int(month) < 10:
                month = '0' + month

            if int(day) < 10:
                day = '0' + day

            date = year + '-' + month + '-' + day

            expense.title = title
            expense.date = date
            expense.amount = amount
            expense.description = description

            expense.save()

            return redirect(reverse('my_app:main'))
        
    else:
        form = EditForm()
        expense = models.Expense.objects.get(pk=int(target))
        context = {'expense': expense, 'form': form}
        return render(request, 'my_app/edit.html', context=context)

def add(request):

    return render(request, 'my_app/add.html')