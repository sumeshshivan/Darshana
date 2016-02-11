from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'darsana/index.html')

def contact(request):
    return render(request, 'darsana/contact.html')
