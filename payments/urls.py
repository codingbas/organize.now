# payments/urls.py

from django.conf.urls import url, include

from payments.views import create_payment

urlpatterns = [
    url(r'^payment/', create_payment, name="create_payment"),
]

