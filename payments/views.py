from django.shortcuts import render
from django.conf import settings # new
import stripe # new

stripe.api_key = settings.STRIPE_SECRET_KEY # new

# Create your views here.
def create(request):
    """Return the create-payment.html file"""
    stripe_id = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,  'create-payment.html', { "stripe_id": stripe_id })

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3000,
            currency='eur',
            description='Premium membership',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

    