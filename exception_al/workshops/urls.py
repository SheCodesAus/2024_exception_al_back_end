from django.urls import path, include # This imports the path and include functions from the django.urls module
from .views import WorkshopListView, WorkshopDetailView, WorkshopViewSet # This imports the WorkshopListView and WorkshopDetailView views from the views.py file in the workshops app
urlpatterns = [
    # path('workshops/', WorkshopCreateView.as_view(), name='workshop-create'), # This maps the URL /workshops/ to the WorkshopCreateView view
    path('workshops/', WorkshopListView.as_view()), # This maps the URL /workshops/ to the WorkshopListView view
    path('workshops/<int:pk>/', WorkshopDetailView.as_view()), # This maps the URL /workshops/<int:pk>/ to the WorkshopDetailView view
    path('workshops/<str:workshop_category>/', WorkshopViewSet.as_view({'get': 'list'})), # This maps the URL /workshops/<str:workshop_category>/ to the WorkshopViewSet view
]