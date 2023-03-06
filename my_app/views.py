from django.shortcuts import render
from django.http.response import HttpResponse
from . import models
from .forms import DateForm

# Create your views here.

def landing(request):
    return render(request, 'my_app/landing.html')

def main(request):
    form = DateForm()
    if (request.GET):
        data = request.GET
        print(type(data['date']))
        targetDate = data['date']
        all_expenses = models.Expense.objects.filter(date=targetDate)
    else:
        all_expenses = models.Expense.objects.all()
    
    context = {'expenses': all_expenses, 'form': form}
    return render(request,'my_app/main.html',context=context)      
    


def edit(request):
    return render(request, 'my_app/edit.html')
