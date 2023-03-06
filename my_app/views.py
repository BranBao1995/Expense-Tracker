from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# Create your views here.

def landing(request):
    return render(request, 'my_app/landing.html')

def main(request):
    all_expenses = models.Expense.objects.all() 
    context = {'expenses':all_expenses}

    return render(request,'my_app/main.html',context=context)

def edit(request):
    return render(request, 'my_app/edit.html')
