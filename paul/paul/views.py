from django.http import HttpResponse

"""
Returns a basic Hello World HTTP response for the homepage.
"""
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')