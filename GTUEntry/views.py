from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from faculty.models import *
from .forms import GTUExamDataForm
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from authenticate.decorators import role_required

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


@login_required()
@role_required(['admin','gtu_cordinator'])
def exam_entry(request):
    exam = gtu_th_exam_data.objects.all()  # Fetch all exams
    return render(request,'view_exams.html',{'exam': exam})

@login_required()
@role_required(['admin','gtu_cordinator'])
def exam_views(request):
    exam = gtu_th_exam_data.objects.all()  # Fetch all exams
    return render(request,'exam_edit_view.html',{'exam': exam})



@login_required()
@role_required(['admin'])
def edit_exam(request,exam_id):
    exam_obj = get_object_or_404(gtu_th_exam_data, pk=exam_id)
    if request.method == 'POST':
        form = GTUExamDataForm(request.POST, instance=exam_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "exam updated successfully!")
            return redirect('exam_entry')
        # else:
        #     messages.error(request, "Please correct the errors below.")
    else:
        form = GTUExamDataForm(instance=exam_obj)
    return render(request,'edit_exam.html', {'form': form})
