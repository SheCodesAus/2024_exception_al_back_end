from django.urls import path, include # This imports the path and include functions from the django.urls module
from .views import WorkshopCreateView , WorkshopListView  # This imports the WorkshopCreateView and WorkshopListView views from the workshops.views module


urlpatterns = [
    path('workshops/', WorkshopCreateView.as_view(), name='workshop-create'), # This maps the URL /workshops/ to the WorkshopCreateView view
    path('workshops/', WorkshopListView.as_view(), name='workshop-list'), # This maps the URL /workshops/ to the WorkshopListView view

]