from django.shortcuts import render, redirect
from faculty.forms import ExamForm

def add_exam(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or another view
    else:
        form = ExamForm()

    return render(request, 'add_exam.html', {'form': form})

