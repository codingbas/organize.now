# payments/urls.py

from django.conf.urls import url, include

from payments.views import create, charge

urlpatterns = [
    url(r'^create', create, name="create"),
    url(r'^charge', charge, name="charge"),
]

