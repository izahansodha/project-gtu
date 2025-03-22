from django.http import response
from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from .forms import CustomUserCreationForm,CustomLoginForm,AdminPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from authenticate.models import custumuser
from django.contrib import messages
from .forms import CustomUserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



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

def user_record(request):
    users = custumuser.objects.all()  #Fetch all users
    return render(request, 'user.html', {'users': users})


def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    users = custumuser.objects.all()  # Fetch all users
    return render(request, 'home.html', {'users': users}) 

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

def user_data(request,pk):
    if request.user.is_authenticated:
           user_record = custumuser.objects.get(id=pk)
           return render(request,'user_data.html',{'user_record':user_record})
    else:
        messages.success(request,"you must be login to view this page")
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = custumuser.objects.get(id=pk)
        form = CustomUserCreationForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record update Successfully ...")
            return redirect('user')
        return render(request,'update_user.html',{'form':form})
    else:
       messages.success(request,"you must be login to do that thing...")
       return render('user.html')
    



def edit_user(request, user_id):
    user = get_object_or_404(custumuser, id=user_id)  # Get user by ID

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save updated user data
            return redirect('home')  # Redirect after successful edit
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'edit-user.html', {'form': form})

User = get_user_model()

@login_required
def change_user_password(request, user_id):
    if not request.user.is_superuser:  # Ensure only admins can change passwords
        return redirect('home')

    user = get_object_or_404(User, id=user_id)  # Get the user by ID

    if request.method == 'POST':
        form = AdminPasswordChangeForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after successful update
    else:
        form = AdminPasswordChangeForm(user=user)

    return render(request, 'change_password.html', {'form': form, 'user': user})

