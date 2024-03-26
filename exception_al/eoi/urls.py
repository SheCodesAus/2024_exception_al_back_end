from django.urls import path
from . import views

urlpatterns = [
    path('eoi/', views.EoiList.as_view()),
    ]