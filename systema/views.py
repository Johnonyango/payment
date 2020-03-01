from django.shortcuts import render
from django.http import HttpResponse


def payment(request):
    return HttpResponse('<h1> This is a payment system<h1/>')