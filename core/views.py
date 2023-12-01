from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
    email = request.POST['email']
    username= request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    
  else:
    return render(request, 'signup.html')
