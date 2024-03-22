from django.urls import path, include # This imports the path and include functions from the django.urls module
from .views import WorkshopCreateView # This imports the WorkshopCreateView class from the views.py file


urlpatterns = [
    path('workshops/', WorkshopCreateView.as_view(), name='workshop-create'), # This maps the URL /workshops/ to the WorkshopCreateView view
    
]