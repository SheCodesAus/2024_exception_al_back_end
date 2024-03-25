"""
URL configuration for exception_al project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
=======
<<<<<<< HEAD
from django.urls import path,include
from .views import CustomAuthToken

=======
from django.urls import path, include
from user.views import CustomAuthToken
>>>>>>> ddba3410447f466059efc3d582808a8ff041ef73
>>>>>>> 460ba60d040086b769b2f4328023934d557627b7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workshops.urls')), # This includes the workshops.urls module in the root URL configuration
    path('', include ('user.urls')),
<<<<<<< HEAD
    path('api-auth/', include('rest_framework.urls')), # This includes the rest_framework.urls module in the root URL configuration

=======
<<<<<<< HEAD
    path('api-auth/', include('rest_framework.urls')), # This includes the rest_framework.urls module in the root URL configuration
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'), # This maps the URL /api-token-auth/ to the CustomAuthToken view
    
=======
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth')
>>>>>>> ddba3410447f466059efc3d582808a8ff041ef73
>>>>>>> 460ba60d040086b769b2f4328023934d557627b7
]
