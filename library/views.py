from django.shortcuts import render, redirect
from django.http import response
from .forms import UserForm

# Create your views here.
def landing(request):
    return render(request,'landing.html')


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'createuser.html', {'form': form})

def success(request):
    return render(request,'success.html')

def login(request):
    return render(request, 'login.html')