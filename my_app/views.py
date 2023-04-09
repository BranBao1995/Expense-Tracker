from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm 
from . import models
from .forms import DateForm, EditForm, AddForm


# Create your views here.


# Manual login view
# def auth_login(request):

#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             return redirect(reverse('my_app:landing')) 
#         else:
#             return HttpResponse('Error Logging In')

#     return render(request, 'my_app/login.html')

def signup_user(request):

    context = None

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            form.save()
            return redirect(reverse('my_app:landing'))
        
    else:

        form = UserCreationForm()
        context = {'form': form}

    return render(request, 'my_app/signup.html', context=context)


def landing(request):
    return render(request, 'my_app/landing.html')


@login_required
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
        all_expenses = models.Expense.objects.filter(author=request.user.id)
    
    context = {'expenses': all_expenses, 'form': form}
    return render(request,'my_app/main.html',context=context)      
    

# Using model form

@login_required
def edit(request, target):

    context = None

    if request.method == 'POST':
        
        instance = models.Expense.objects.get(pk=int(target))
        form = EditForm(request.POST, instance=instance)
        context = {'form': form}

        if form.is_valid():

            try:
                form.save()
            except:
                return HttpResponse('Error saving form.')
            else:
                return redirect(reverse('my_app:main'))
                
    else:
        expense = models.Expense.objects.get(pk=int(target))
        form = EditForm(instance = expense)
        
        context = {'form': form}
        
    return render(request, 'my_app/edit.html', context=context)


@login_required
def add(request):

    context = None

    if request.method == 'POST':

        form = AddForm(request.POST)
        context = {'form': form}

        for field in form:
            print(field.value())

        if form.is_valid():

            try:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
            except ValueError:
                return HttpResponse('ValueError')
            else:   
                return redirect(reverse('my_app:main'))
    else:

        form = AddForm()
        context = {'form': form}
        
    return render(request, 'my_app/add.html', context=context)




#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------




# When Model Form is not used, make sure Django Form validations are consistent with Model Field validations
# Because Model Field validatons will not be run automatically
# If form validations allow data to pass, then these data will be stored into your DB regardless of Model Field Validations
# Unless DB-side validations are present, but then that will throw an exception


# Using Django form but not model form
# def add(request):

#     if request.method == 'POST':
#         form = AddForm(request.POST)

#         if form.is_valid():

#             title = request.POST['title']
#             year = request.POST['date_year']
#             month = request.POST['date_month']
#             day = request.POST['date_day']
#             amount = request.POST['amount']
#             description = request.POST['description']
    

#             if int(month) < 10:
#                 month = '0' + month

#             if int(day) < 10:
#                 day = '0' + day

#             date = year + '-' + month + '-' + day

#             try:
#                 # models.Expense.objects.create(title = title, date = date, amount = amount, description = description)
#                 instance = models.Expense(title = title, date = date, amount = -15, description = description)
#                 instance.full_clean()
#             except ValidationError:
#                 print('Error!')
#                 return HttpResponse('There is an error.')
#             else:
#                 instance.save()
#                 return redirect(reverse('my_app:main'))
        
#     else:
#         form = AddForm()
#         context = {'form': form}
#         return render(request, 'my_app/add.html', context=context)




# When neither Model Form nor Django Form is used, model field validations need to be run manually
# def add(request):

#     if request.method == 'POST':

#         title = request.POST['title']
#         date = request.POST['date']
#         amount = request.POST['amount']
#         description = request.POST['description']

#         instance = models.Expense(title = title, date = date, amount = amount, description = description)

#         try:
#             instance.full_clean()
#         except ValidationError:
#             # return to landing page when it doesnt pass validation
#             print(ValidationError)
#             return redirect(reverse('my_app:landing'))
#         else:
#             instance.save()
#             return redirect(reverse('my_app:main'))

#     else:
#         return render(request, 'my_app/add.html')


# def edit(request, target):

#     if request.method == 'POST':
        
#         form = EditForm(request.POST)

#         if form.is_valid():
#             expense = models.Expense.objects.get(pk=int(target))

#             title = request.POST['title']
#             amount = request.POST['amount']
#             description = request.POST['description']
#             year = request.POST['date_year']
#             month = request.POST['date_month']
#             day = request.POST['date_day']

#             if int(month) < 10:
#                 month = '0' + month

#             if int(day) < 10:
#                 day = '0' + day

#             date = year + '-' + month + '-' + day

#             expense.title = title
#             expense.date = date
#             expense.amount = int(amount)
#             expense.description = description

#             try:
#                 expense.full_clean()
#             except ValidationError:
#                 print('Error!')
#                 return HttpResponse('There is an error.')
#             else:
#                 expense.save()
#                 return redirect(reverse('my_app:main'))
        
#     else:
#         expense = models.Expense.objects.get(pk=int(target))
#         data_dict = {'title': expense.title, 'date': expense.date, 'amount': expense.amount, 'description': expense.description}
#         form = EditForm(initial=data_dict)
        
#         context = {'expense': expense, 'form': form}
#         return render(request, 'my_app/edit.html', context=context)