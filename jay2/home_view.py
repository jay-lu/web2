from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, new home page!")
    return render(request, 'home/home.html', {})