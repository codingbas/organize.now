from django.shortcuts import render, redirect, reverse

"""
This view is to determine a redirect based on a user being signed in or not signed in
"""
def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('todolist'))
    else:
        return redirect(reverse('login'))