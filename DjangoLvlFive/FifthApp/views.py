import django.urls.exceptions
from django.shortcuts import render
from FifthApp.forms import UserForm, UserProfileInfoForm

# For Login Page
from django.urls import reverse  # do not use django.core.urls
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login an failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid Login details")
    return render(request, 'user_login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:home'))


def register(request):
    registered = False  # This is saying that the user is not registered
    if request.method == 'POST':  # When request is equal to POST then we take the information
        user_form = UserForm(data=request.POST)  # Get information from the user form
        profile_form = UserProfileInfoForm(
            data=request.POST)  # Gets information from the profile form(Make sure the name is unique)
        if user_form.is_valid() and profile_form.is_valid():  # This checks that both forms are valid

            user = user_form.save()  # Saves information  directly to the database
            user.set_password(user.password)  # Hashes the password
            user.save()  # This saves th echages to the database

            profile = profile_form.save(
                commit=False)  # Directly saves to the database. Don't commit to the database yet otherwise we may get
            # collision errors
            profile.user = user  # Sets up a one-to-one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()  # Saves the model
            registered = True  # The user is now registered
        else:
            print(user_form.errors, profile_form.errors)

    else:  # This mean the request was actually a http request
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def other(request):
    return render(request, 'other.html')
