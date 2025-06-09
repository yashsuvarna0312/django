from django.shortcuts import render , redirect

from django.http import HttpResponse

from .models import UserProfile

def Home(request):
    return HttpResponse("Welcome to codeswithpankaj")


def About(request):
    return HttpResponse("welcome to about us")


def contact(request):
    return render(request,'contactus.html')





def display_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})