from django.http import response
from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomUserCreationForm,CustomLoginForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Custom authentication
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'home.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = CustomLoginForm()
        return render(request, 'home.html', {'form': form})
    
    return render(request,"home.html")


def user_logout(request):
    logout(request)
    return redirect('home')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save the user object but don't commit yet
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()  # Now save the user
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Debugging: Print errors to the console

    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
