# apps/seguimiento/models.py
from django.db import models

class SeguimientoAT(models.Model):
    # Materias reprobadas 
    num_subject_failed = models.IntegerField()

    # Parciales por materia 
    m1_p1 = models.BooleanField(default=False)
    m1_p2 = models.BooleanField(default=False)
    m1_p3 = models.BooleanField(default=False)
    m1_p4 = models.BooleanField(default=False)
    m2_p1 = models.BooleanField(default=False)
    m2_p2 = models.BooleanField(default=False)
    m2_p3 = models.BooleanField(default=False)
    m2_p4 = models.BooleanField(default=False)
    m3_p1 = models.BooleanField(default=False)
    m3_p2 = models.BooleanField(default=False)
    m3_p3 = models.BooleanField(default=False)
    m3_p4 = models.BooleanField(default=False)
    m4_p1 = models.BooleanField(default=False)
    m4_p2 = models.BooleanField(default=False)
    m4_p3 = models.BooleanField(default=False)
    m4_p4 = models.BooleanField(default=False)
    m5_p1 = models.BooleanField(default=False)
    m5_p2 = models.BooleanField(default=False)
    m5_p3 = models.BooleanField(default=False)
    m5_p4 = models.BooleanField(default=False)
    m6_p1 = models.BooleanField(default=False)
    m6_p2 = models.BooleanField(default=False)
    m6_p3 = models.BooleanField(default=False)
    m6_p4 = models.BooleanField(default=False)
    m7_p1 = models.BooleanField(default=False)
    m7_p2 = models.BooleanField(default=False)
    m7_p3 = models.BooleanField(default=False)
    m7_p4 = models.BooleanField(default=False)

    # Factores por los que el alumno es considerado como vulnerable
    inasistencias = models.BooleanField(default=False)
    Incumplimiento_de_entregables = models.BooleanField(default=False)
    Poco_Interés_en_las_Asignaturas_con_problemas = models.BooleanField(default=False)
    Emocionales_o_Psicológicos = models.BooleanField(default=False)
    Carta_compromiso = models.BooleanField(default=False)
    Problemas_Familiares = models.BooleanField(default=False)
    Bajos_Ingreso = models.BooleanField(default=False)
    Trabaja = models.BooleanField(default=False)
    Padre_o_Madre_de_familia = models.BooleanField(default=False)

    # Acciones sugeridas con Base al diagnóstico
    AT_AC_Académico = models.BooleanField(default=False)
    AT_AC_Personal = models.BooleanField(default=False)
    AT_AC_Socioeconómico = models.BooleanField(default=False)

    # Resultado de la acción Tutorial - Alumno Retenido
    RT_AR_Académico = models.BooleanField(default=False)
    RT_AR_Personal = models.BooleanField(default=False)
    RT_AR_Socioeconómico = models.BooleanField(default=False)

    # Observaciones
    Observaciones = models.TextField()

    # Métodos para calcular sumatorias
    def calculate_failed_subjects(self):
        subjects = [
            [self.m1_p1, self.m1_p2, self.m1_p3, self.m1_p4],
            [self.m2_p1, self.m2_p2, self.m2_p3, self.m2_p4],
            [self.m3_p1, self.m3_p2, self.m3_p3, self.m3_p4],
            [self.m4_p1, self.m4_p2, self.m4_p3, self.m4_p4],
            [self.m5_p1, self.m5_p2, self.m5_p3, self.m5_p4],
            [self.m6_p1, self.m6_p2, self.m6_p3, self.m6_p4],
            [self.m7_p1, self.m7_p2, self.m7_p3, self.m7_p4],
        ]
        failed_subjects = sum(1 for subject in subjects if sum(subject) > 2)
        return failed_subjects

    def save(self, *args, **kwargs):
        self.num_subject_failed = self.calculate_failed_subjects()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SeguimientoAT {self.id}"
