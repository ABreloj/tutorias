# apps/seguimiento/views.py
from django.shortcuts import render, redirect
from apps.group.models import Group
from apps.academy.models import Student, Professor
from .models import SeguimientoAT
from apps.career.models import Career
from .forms import SeguimientoForm

def seguimiento_view(request):
    user = request.user
    #careers = Career.objects.all()
    #students = Student.objects.all()
    professor = user.professor
    group = professor.group_set.all().first()
    form = SeguimientoForm()
    career = group.career
    students = group.estudiantes.all()
    period = group.period

    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guarda los datos del formulario en la base de datos
            return redirect('seguimiento')  # Redirige después de guardar
    else:
        form = SeguimientoForm()

    return render(request, 'seguimiento/seguimiento.html', {
        'form': form,
        'career': career,
        'students': students,
        'professor': professor,
        'group': group,
        'period': period,
    })
