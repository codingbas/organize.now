from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

def create_payment(request):
    """Return the create-payment.html file"""
    return render(request,  'create-payment.html')