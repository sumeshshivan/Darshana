from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def sms(request):
    return HttpResponse("sms Home!")
