from django.urls import path, include # This imports the path and include functions from the django.urls module
from rest_framework import routers
from .views import  UserViewSet,WorkshopViewSet,WorkshopListView, WorkshopDetailView, WorkshopViewSet # This imports the WorkshopListView and WorkshopDetailView views from the views.py file in the workshops app

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user') # This registers the UserViewSet view with the router
router.register(r'workshops', WorkshopViewSet, basename='workshop') # This registers the WorkshopViewSet view with the router





urlpatterns = [
    path('', include(router.urls)), # This includes all the URLs from the router  
    path('workshops/', WorkshopListView.as_view()), # This maps the URL /workshops/ to the WorkshopListView view
    path('workshops/<int:pk>/', WorkshopDetailView.as_view()), # This maps the URL /workshops/<int:pk>/ to the WorkshopDetailView view
    path('workshops/<str:workshop_category>/', WorkshopViewSet.as_view({'get': 'list'})), # This maps the URL /workshops/<str:workshop_category>/ to the WorkshopViewSet view
]