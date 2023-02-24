from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def landing(request):
    return render(request, 'my_app/landing.html')

def main(request):
    return render(request, 'my_app/main.html')

def edit(request):
    return render(request, 'my_app/edit.html')