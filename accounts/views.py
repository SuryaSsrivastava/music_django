from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as login_, logout as logout_
from accounts.models import Account
from music.models import Album,Song
from accounts.forms import UserForm,RegistrationForm

def home(request):

    context ={}

    user = Account.objects.all()
    context['user'] = user

    return render(request,'accounts/base.html',context)

def login(request):

    if request.method == "POST":
    
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login_(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')



def logout(request):
    logout_(request)
    form = UserForm(request.POST)
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)

def register(request):

    form = RegistrationForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password )
        if user is not None:
            if user.is_active:
                login_(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)




