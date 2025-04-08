from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from faculty.models import *
from .forms import GTUExamDataForm, GTUExamCPForm
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authenticate.decorators import role_required
from django.template.loader import render_to_string
from django.http import HttpResponse

# def exam_data_view(request):
#     form = GTUExamDataForm()
#     return render(request, 'add_th_exam_entry.html', {'form': form})

@login_required()
@role_required(['admin','gtu_cordinator'])
def exam_data_view(request):
    # Get active faculty to display initially
    active_faculty = faculty.objects.filter(is_active=True).order_by('full_name')
    initial_data = {'date': date.today()}

    if request.method == 'POST':
        form = GTUExamDataForm(request.POST)
        if form.is_valid():
            form.save()
            # Add success message or redirect
    else:
        form = GTUExamDataForm(initial=initial_data)

    return render(request, 'add_th_exam_entry.html', {
        'form': form,
        'active_faculty': active_faculty  # Pass active faculty to template
    })


@login_required()
@role_required(['admin','gtu_cordinator'])
def load_times(request):
    session_id = request.GET.get('session_id')
    times = time.objects.filter(session_id=session_id).order_by('time')
    return render(request, 'times_dropdown.html', {'times': times})


# def load_faculty(request):
#     search = request.GET.get('search', '')
#     if search:
#         faculty_list = faculty.objects.filter(
#             is_active=True,
#             full_name__icontains=search
#         ).order_by('full_name')
#     else:
#         faculty_list = faculty.objects.filter(is_active=True).order_by('full_name')
#
#     return render(request, 'faculty_dropdown.html', {'faculty_list': faculty_list})

@login_required()
@role_required(['admin','gtu_cordinator'])
def load_faculty(request):
    search_term = request.GET.get('search', '')
    faculty_list = faculty.objects.filter(is_active=True)

    if search_term:
        faculty_list = faculty_list.filter(
            models.Q(full_name__icontains=search_term) |
            models.Q(short_name__icontains=search_term)
        )

    return render(request, 'faculty_dropdown.html', {
        'faculty_list': faculty_list.order_by('full_name')
    })


# @login_required()
# @role_required(['admin','gtu_cordinator'])
# def exam_entry(request):
#     exam = gtu_th_exam_data.objects.all()  # Fetch all exams
#     return render(request,'view_exams.html',{'exam': exam})


# @login_required()
# @role_required(['admin', 'gtu_cordinator'])
# def exam_views(request):
#     exam = gtu_th_exam_data.objects.all()  # Fetch all exams
#     return render(request,'exam_edit_view.html',{'exam': exam})
@login_required()
@role_required(['admin', 'gtu_cordinator'])
def exam_views(request):
    exam_id = request.GET.get("exam_id")
    if exam_id:
        exam = gtu_th_exam_data.objects.filter(exam_id=exam_id)
    else:
        exam = gtu_th_exam_data.objects.all()

    exams_list = exam_name.objects.all().order_by('-id')

    # If it's an HTMX request, return only the partial HTML
    if request.headers.get('HX-Request'):
        html = render_to_string('_exam_table_partial.html', {'exam': exam})
        return HttpResponse(html)

    # Otherwise, render full page
    return render(request, 'exam_edit_view.html', {
        'exam': exam,
        'exams_list': exams_list,
    })


@login_required()
@role_required(['admin', 'gtu_cordinator'])
def edit_exam(request,exam_id):
    exam_obj = get_object_or_404(gtu_th_exam_data, pk=exam_id)
    if request.method == 'POST':
        form = GTUExamDataForm(request.POST, instance=exam_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "exam updated successfully!")
            return redirect('exam_views')
        # else:
        #     messages.error(request, "Please correct the errors below.")
    else:
        form = GTUExamDataForm(instance=exam_obj)
    return render(request,'edit_exam.html', {'form': form})


@login_required()
@role_required(['admin', 'gtu_cordinator'])
def add_gtu_exam_cp(request):
    initial_date = {'date': date.today()}
    if request.method == 'POST':
        form = GTUExamCPForm(request.POST)
        subject_data = {}
        grand_total = 0

        # Extract all subject data from POST manually
        for i in range(1, 13):
            code_key = f'sub_{i}_code'
            name_key = f'sub_{i}_name'
            students_key = f'sub{i}_no_of_student'
            pages_key = f'sub{i}_no_of_pages'

            code = request.POST.get(code_key, '').strip()
            name = request.POST.get(name_key, '').strip()

            try:
                students = int(request.POST.get(students_key, 0))
            except ValueError:
                students = 0
            try:
                pages = int(request.POST.get(pages_key, 0))
            except ValueError:
                pages = 0

            subject_data[code_key] = code
            subject_data[name_key] = name
            subject_data[students_key] = students
            subject_data[pages_key] = pages

            grand_total += students * pages

        if form.is_valid():
            instance = form.save(commit=False)

            # Apply manual fields to the instance
            for key, value in subject_data.items():
                setattr(instance, key, value)

            instance.total_pages = grand_total
            instance.save()
            messages.success(request, "Data saved successfully.")
            return redirect('add_gtu_exam_cp')

        else:
            # Form is invalid, return all subject data to the template
            messages.error(request, "There was an error submitting the form. Please correct the issues below.")
            return render(request, 'exam_cp_data_form.html', {
                'form': form,
                'subject_range': range(1, 13),
                'subject_data': subject_data,  # optional, not used in template
            })

    else:
        form = GTUExamCPForm(initial=initial_date)
        return render(request, 'exam_cp_data_form.html', {
            'form': form,
            'subject_range': range(1, 13),
        })

@login_required()
@role_required(['admin', 'gtu_cordinator'])
def cp_exam_views(request):
    exam_id = request.GET.get("exam_id")
    if exam_id:
        cp_data = gtu_th_CP_data.objects.filter(exam_id=exam_id)
    else:
        cp_data = gtu_th_CP_data.objects.all()

    exams_list = exam_name.objects.all().order_by('-id')

    if request.headers.get('HX-Request'):
        html = render_to_string('_cp_table_partial.html', {'cp_data': cp_data})
        return HttpResponse(html)

    return render(request, 'cp_exam_view.html', {
        'cp_data': cp_data,
        'exams_list': exams_list,
    })


@login_required()
@role_required(['admin', 'gtu_cordinator'])
def edit_cp_exam(request, cp_id):
    cp_obj = get_object_or_404(gtu_th_CP_data, pk=cp_id)
    if request.method == 'POST':
        form = GTUExamCPForm(request.POST, instance=cp_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "CP exam updated successfully!")
            return redirect('cp_exam_views')
    else:
        form = GTUExamCPForm(instance=cp_obj)
    return render(request, 'edit_cp_exam.html', {'form': form})