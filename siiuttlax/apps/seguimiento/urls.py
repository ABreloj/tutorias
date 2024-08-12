# apps/seguimiento/urls.py

from django.urls import path
from .views import seguimiento_view

urlpatterns = [
    path('', seguimiento_view, name='seguimiento'),  # Vista principal
]
