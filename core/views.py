from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = aut
  return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
    email = request.POST['email']
    username= request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    
    if password == password2:
      if User.objects.filter(email=email).exisits():
        messages.info(request, 'Email taken')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, 'Username is taken')
        return redirect('signup')
      else:
        user = User.object.create_user(username=username, email=email, password=password)
        user.save()
        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)
        return redirect('/')
    else:
      messages.info(request, 'Password not matching')
      return redirect('signup')    
  else:
    return render(request, 'signup.html')
