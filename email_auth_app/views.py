from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from email_auth_app.models import Token
from django.core.mail import EmailMessage
import os, binascii
from django.contrib.auth import login, authenticate, logout


def index(request):

    if request.user.is_authenticated():
        return render(request, "logged_in.html", {'name': request.user.first_name})
    else:
        return render(request, "index.html", {})


def login_view(request):
    username = request.POST['username']
    user = User.objects.get(username=username)
    token = Token()
    token.username = username
    token.token = binascii.b2a_hex(os.urandom(25))

    #TODO: should do something to check that the token is unique
    token.save()

    email = EmailMessage('Login link',
    'Login Here: http://127.0.0.1:8000/login_token?token=' + token.token
    + '&username=' + user.username,
    to=[user.email])
    email.send()
    return render(request, "email_sent.html", {'email': username})


def login_token(request):
    #TODO: validate that the token exists and that it isn't expired
    token = Token.objects.get(pk=request.GET['token'], username=request.GET['username'])

    user = authenticate(username=request.GET['username'], password='password')
    login(request, user)

    return redirect('/')

def signup(request):
    return render(request, "new_user.html", {})


def create_user(request):
    #TODO: verify that this user input is valid.
    username = request.POST['username']
    email = request.POST['email']
    name = request.POST['name']
    user = User.objects.create_user(username, email, 'password')
    user.first_name = name
    user.save()

    user = authenticate(username=username, password='password')
    login(request, user)

    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

