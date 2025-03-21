from django.http import response
from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomUserCreationForm,CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

def login_user(request):
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
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = CustomLoginForm()
        return render(request, 'login.html', {'form': form})
    return render(request,"login.html",{'form': form})

def header(request):
    role = None  # Default role is None

    if request.user.is_authenticated:
        role = request.user.role  # Correct way to access role

    return render(request, "header.html", {'role': role})



def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save the user object but don't commit yet
            
            if not user.role:  # Ensure a role is set
                user.role = 'department'  # Set default role if missing
            
            print(f"User Role Before Save: {user.role}")  # Debugging

            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()  # Now save the user

            # Assign user to a group based on role
            role_to_group = {
                'admin': 'Admin',
                'gtu_cordinator': 'GTU Coordinator',
                'department': 'Department'
            }

            group_name = role_to_group.get(user.role)
            if group_name:
                group, _ = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)

            print(f"User Role After Save: {user.role}")  # Debugging
            print(f"Assigned Group: {group_name}")  # Debugging

            login(request, user)
            return redirect('home')

        else:
            print(form.errors)  # Debugging: Print errors to console

    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

