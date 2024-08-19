# Generated by Django 5.0.6 on 2024-07-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte_tutoria', '0002_alter_reportetutoria_evidencia1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportetutoria',
            name='evidencia4',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/', verbose_name='Evidencia pdf_canalizacion'),
        ),
        migrations.AlterField(
            model_name='reportetutoria',
            name='evidencia3',
            field=models.FileField(blank=True, null=True, upload_to='evidencias/', verbose_name='Evidencia de audio'),
        ),
    ]
