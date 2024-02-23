from django.shortcuts import render
from django.http import response

# Create your views here.
def landing(request):
    return render(request,'landing.html')