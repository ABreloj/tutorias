# apps/seguimiento/views.py
from django.shortcuts import render, redirect
from apps.group.models import Group
from apps.academy.models import Student, Professor
from .models import SeguimientoAT
from apps.career.models import Career
from .forms import SeguimientoForm

def seguimiento_view(request):
    user = request.user
    professor = user.professor
    group = professor.group_set.all().first()
    career = group.career
    students = group.estudiantes.all()
    period = group.period

    if request.method == 'POST':
        
        for student in students:
            # Contador de materias reprobadas
            num_subject_failed = 0

            # Materias por parcial
            m1p1 = f'm1p1-{student.id}'
            valm1p1 = request.POST.get(m1p1) == 'on'
            m1p2 = f'm1p2-{student.id}'
            valm1p2 = request.POST.get(m1p2) == 'on'
            m1p3 = f'm1p3-{student.id}'
            valm1p3 = request.POST.get(m1p3) == 'on'
            m1p4 = f'm1p4-{student.id}'
            valm1p4 = request.POST.get(m1p4) == 'on'

            m2p1 = f'm2p1-{student.id}'
            valm2p1 = request.POST.get(m2p1) == 'on'
            m2p2 = f'm2p2-{student.id}'
            valm2p2 = request.POST.get(m2p2) == 'on'
            m2p3 = f'm2p3-{student.id}'
            valm2p3 = request.POST.get(m2p3) == 'on'
            m2p4 = f'm2p4-{student.id}'
            valm2p4 = request.POST.get(m2p4) == 'on'

            m3p1 = f'm3p1-{student.id}'
            valm3p1 = request.POST.get(m3p1) == 'on'
            m3p2 = f'm3p2-{student.id}'
            valm3p2 = request.POST.get(m3p2) == 'on'
            m3p3 = f'm3p3-{student.id}'
            valm3p3 = request.POST.get(m3p3) == 'on'
            m3p4 = f'm3p4-{student.id}'
            valm3p4 = request.POST.get(m3p4) == 'on'

            m4p1 = f'm4p1-{student.id}'
            valm4p1 = request.POST.get(m4p1) == 'on'
            m4p2 = f'm4p2-{student.id}'
            valm4p2 = request.POST.get(m4p2) == 'on'
            m4p3 = f'm4p3-{student.id}'
            valm4p3 = request.POST.get(m4p3) == 'on'
            m4p4 = f'm4p4-{student.id}'
            valm4p4 = request.POST.get(m4p4) == 'on'

            m5p1 = f'm5p1-{student.id}'
            valm5p1 = request.POST.get(m5p1) == 'on'
            m5p2 = f'm5p2-{student.id}'
            valm5p2 = request.POST.get(m5p2) == 'on'
            m5p3 = f'm5p3-{student.id}'
            valm5p3 = request.POST.get(m5p3) == 'on'
            m5p4 = f'm5p4-{student.id}'
            valm5p4 = request.POST.get(m5p4) == 'on'

            m6p1 = f'm6p1-{student.id}'
            valm6p1 = request.POST.get(m6p1) == 'on'
            m6p2 = f'm6p2-{student.id}'
            valm6p2 = request.POST.get(m6p2) == 'on'
            m6p3 = f'm6p3-{student.id}'
            valm6p3 = request.POST.get(m6p3) == 'on'
            m6p4 = f'm6p4-{student.id}'
            valm6p4 = request.POST.get(m6p4) == 'on'

            m7p1 = f'm7p1-{student.id}'
            valm7p1 = request.POST.get(m7p1) == 'on'
            m7p2 = f'm7p2-{student.id}'
            valm7p2 = request.POST.get(m7p2) == 'on'
            m7p3 = f'm7p3-{student.id}'
            valm7p3 = request.POST.get(m7p3) == 'on'
            m7p4 = f'm7p4-{student.id}'
            valm7p4 = request.POST.get(m7p4) == 'on'

            # Incrementa el contador por cada materia reprobada
            if valm1p1 or valm1p2 or valm1p3 or valm1p4:
                num_subject_failed += 1
            if valm2p1 or valm2p2 or valm2p3 or valm2p4:
                num_subject_failed += 1
            if valm3p1 or valm3p2 or valm3p3 or valm3p4:
                num_subject_failed += 1
            if valm4p1 or valm4p2 or valm4p3 or valm4p4:
                num_subject_failed += 1
            if valm5p1 or valm5p2 or valm5p3 or valm5p4:
                num_subject_failed += 1
            if valm6p1 or valm6p2 or valm6p3 or valm6p4:
                num_subject_failed += 1
            if valm7p1 or valm7p2 or valm7p3 or valm7p4:
                num_subject_failed += 1

            student.num_subject_failed = num_subject_failed

            # Crear o actualizar el registro de SeguimientoAT
            segui = student.seguimientoat_set.all().first()
            if not segui:
                segui = SeguimientoAT.objects.create(student=student, num_subject_failed=num_subject_failed)
            else:
                segui.num_subject_failed = num_subject_failed

            # Otros campos del formulario
            inasistencias = f'inasistencias-{student.id}'
            valinasistencias = request.POST.get(inasistencias) == 'on'

            inEntregables = f'inEntregables-{student.id}'
            valinEntregables = request.POST.get(inEntregables) == 'on'

            notInteres = f'notInteres-{student.id}'
            valnotInteres = request.POST.get(notInteres) == 'on'

            emocion = f'emocion-{student.id}'
            valemocion = request.POST.get(emocion) == 'on'

            card = f'card-{student.id}'
            valcard = request.POST.get(card) == 'on'

            family = f'family-{student.id}'
            valfamily = request.POST.get(family) == 'on'

            lowIngresos = f'lowIngresos-{student.id}'
            vallowIngresos = request.POST.get(lowIngresos) == 'on'

            work = f'work-{student.id}'
            valwork = request.POST.get(work) == 'on'

            FM = f'FM-{student.id}'
            valFM = request.POST.get(FM) == 'on'

            academy = f'academy{student.id}'
            valacademy = request.POST.get(academy) == 'on'

            personal = f'personal{student.id}'
            valpersonal = request.POST.get(personal) == 'on'

            socioeconomic = f'socioeconomic{student.id}'
            valsocioeconomic = request.POST.get(socioeconomic) == 'on'

            academy2 = f'academy2{student.id}'
            valacademy2 = request.POST.get(academy2) == 'on'

            personal2 = f'personal2{student.id}'
            valpersonal2 = request.POST.get(personal2) == 'on'

            socioeconomic2 = f'socioeconomic2{student.id}'
            valsocioeconomic2 = request.POST.get(socioeconomic2) == 'on'

            observaciones = f'observaciones-{student.id}'
            valobservaciones = request.POST.get(observaciones)

            # Actualización de valores en el objeto SeguimientoAT
            segui.inasistencias = valinasistencias
            segui.Incumplimiento_de_entregables = valinEntregables
            segui.Poco_Interés_en_las_Asignaturas_con_problemas = valnotInteres
            segui.Emocionales_o_Psicológicos = valemocion
            segui.Carta_compromiso = valcard
            segui.Problemas_Familiares = valfamily
            segui.Bajos_Ingreso = vallowIngresos
            segui.Trabaja = valwork
            segui.Padre_o_Madre_de_familia = valFM
            segui.Academicos = valacademy
            segui.Personales = valpersonal
            segui.Socioeconómicos = valsocioeconomic
            segui.Academicos2 = valacademy2
            segui.Personales2 = valpersonal2
            segui.Socioeconomicos2 = valsocioeconomic2
            segui.Observaciones = valobservaciones

            segui.save()

    context = {
        'career': career,
        'period': period,
        'group': group,
        'students': students,
    }
    
    return render(request, 'seguimiento/seguimiento.html', context)
