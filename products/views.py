from django.shortcuts import render
from django.http import  HttpResponse


def index(request):

    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def academics(request):
    return render(request, 'academics.html')


def culture(request):
    return render(request, 'cultureandarts.html')


def feedingprogram(request):
    return render(request, 'feedingprogram.html')


def donate(request):
    return render(request, 'donations.html')


def notifications(request):
    return render(request, 'notifications.html')