from django.shortcuts import render, redirect, get_object_or_404
from faculty.forms import ExamForm, FacultyForm, DepartmentForm
from .models import faculty, department
from django.contrib.auth.decorators import login_required
from authenticate.decorators import role_required
from django.contrib import messages


@login_required()
@role_required(['admin'])
def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or another view
    else:
        form = ExamForm()

    return render(request, 'add_exam.html', {'form': form})


@login_required()
@role_required(['admin'])
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty added successfully!")
            return redirect('faculty_list')
        # else:
        #     messages.error(request, "Please correct the errors below.")
    else:
        form = FacultyForm()

    return render(request, 'add_faculty.html', {'form': form})


@login_required()
@role_required(['admin'])
def faculty_list(request):
    faculties = faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})


@login_required()
@role_required(['admin'])
def edit_faculty(request, faculty_id):
    faculty_obj = get_object_or_404(faculty, pk=faculty_id)

    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty updated successfully!")
            return redirect('faculty_list')
        # else:
        #     messages.error(request, "Please correct the errors below.")
    else:
        form = FacultyForm(instance=faculty_obj)

    return render(request, 'edit_faculty.html', {'form': form})


@login_required()
@role_required(['admin'])
def department_list(request):
    departments = department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


@login_required()
@role_required(['admin'])
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully!")
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})


@login_required()
@role_required(['admin'])
def edit_department(request, dept_id):
    dept = get_object_or_404(department, pk=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'edit_department.html', {'form': form})
