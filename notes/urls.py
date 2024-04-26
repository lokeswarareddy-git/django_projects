from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
    path('details/<int:pk>', views.detail)
]