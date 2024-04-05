from django.urls import path
from . import views

urlpatterns = [
    path('eois/', views.EoiList.as_view()),
    ]