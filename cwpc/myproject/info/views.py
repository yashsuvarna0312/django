from django.shortcuts import render , redirect

from django.http import HttpResponse


def Home(request):
    return HttpResponse("Welcome to codeswithpankaj")


def About(request):
    return HttpResponse("welcome to about us")


def contact(request):
    return render(request,'contactus.html')
