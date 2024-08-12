# apps/seguimiento/forms.py
from django import forms
from .models import SeguimientoAT

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = SeguimientoAT
        fields = [
            'num_subject_failed',
            'm1_p1', 'm1_p2', 'm1_p3', 'm1_p4',
            'm2_p1', 'm2_p2', 'm2_p3', 'm2_p4',
            'm3_p1', 'm3_p2', 'm3_p3', 'm3_p4',
            'm4_p1', 'm4_p2', 'm4_p3', 'm4_p4',
            'm5_p1', 'm5_p2', 'm5_p3', 'm5_p4',
            'm6_p1', 'm6_p2', 'm6_p3', 'm6_p4',
            'm7_p1', 'm7_p2', 'm7_p3', 'm7_p4',


            #Factores por los que el alumno es considerado como vulnerable
            'inasistencias','Incumplimiento_de_entregables','Poco_Interés_en_las_Asignaturas_con_problemas',
            'Emocionales_o_Psicológicos','Carta_compromiso','Problemas_Familiares','Bajos_Ingreso',
            'Trabaja','Padre_o_Madre_de_familia',




            
            #Total de alumnos diagnosticados
            #aqui va la sumatoria pero todavia no queda sigan viendo




            #Acción sugerida con Base al diagnostico
            #aqui va la sumatoria pero todavia no queda sigan viendo




            #Acción Tutorial - Alumno Canalizado
            'AT_AC_Académico','AT_AC_Personal','AT_AC_Socioeconómico',




            #Total de Alumnos canalizados
            #aqui va la sumatoria pero todavia no queda sigan viendo




            #Evidencias de acción tutorial
            #aqui va la sumatoria pero todavia no queda sigan viendo




            #Resultado de la acción Tutorial - Alumno Retenido
            'RT_AR_Académico','RT_AR_Personal','RT_AR_Socioeconómico',






            #Total de Alumnos canalizados
            #aqui va la sumatoria pero todavia no queda sigan viendo



            #Resultados
            #aqui va la sumatoria pero todavia no queda sigan viendo





            #Observaciones
            'Observaciones',



        ]
        widgets = {
            'num_subject_failed': forms.TextInput(attrs={'class': 'form-control'}),
            'm1_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm1_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm1_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm1_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm2_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm2_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm2_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm2_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm3_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm3_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm3_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm3_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm4_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm4_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm4_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm4_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm5_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm5_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm5_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm5_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm6_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm6_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm6_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm6_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm7_p1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm7_p2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm7_p3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'm7_p4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'inasistencias': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Incumplimiento_de_entregables': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Poco_Interés_en_las_Asignaturas_con_problemas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Emocionales_o_Psicológicos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Carta_compromiso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Problemas_Familiares': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Bajos_Ingreso': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Trabaja': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Padre_o_Madre_de_familia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'AT_AC_Académico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'AT_AC_Personal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'AT_AC_Socioeconómico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),



            'RT_AR_Académico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'RT_AR_Personal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'RT_AR_Socioeconómico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),


            'Observaciones': forms.TextInput(attrs={'class': 'form-control'}),
        }