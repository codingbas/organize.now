from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY;

# Create your views here.
def create(request):
    """Return the create-payment.html file"""
    stripe_id = settings.STRIPE_PUBLISHABLE_KEY
    return render(request,  'create-payment.html', { "stripe_id": stripe_id })

def charge(request):
    if request.method == 'POST':
        # do stripe charge
        charge = stripe.Charge.create(
            amount=3000,
            currency='eur',
            description='Premium membership',
            source=request.POST['stripeToken']
        )
        
        # set user.is_premium to 1
        user = User.objects.filter(email=request.user.email).first()
        user.userprofile.is_premium = 1
        user.save()
        
        # return succesful payment response
        return render(request, 'charge.html', { 'post_data': request.POST, 'user': request.user })

    