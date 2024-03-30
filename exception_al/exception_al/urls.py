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
<<<<<<< HEAD
from user.views import CustomAuthToken
=======
=======

from django.urls import path,include
>>>>>>> 13c8170 (worked on exception_al_urls, workshop_views.py)
from .views import CustomAuthToken
>>>>>>> 09fb8f9 ( resolving merge conflict for PR#6)

<<<<<<< HEAD
=======

>>>>>>> 13c8170 (worked on exception_al_urls, workshop_views.py)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('user.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    path('', include('workshops.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth')
=======
    path('api-auth/', include('rest_framework.urls')), # This includes the rest_framework.urls module in the root URL configuration
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'), # This maps the URL /api-token-auth/ to the CustomAuthToken view
    
>>>>>>> 09fb8f9 ( resolving merge conflict for PR#6)
=======
    # path('api-auth/', include('rest_framework.urls')), # This includes the rest_framework.urls module in the root URL configuratio
    path('api-auth/login/', CustomAuthToken.as_view(), name='api_auth_login'), # This maps the URL /api-auth/login/ to the CustomAuthToken view
    path('api-auth/logout/', CustomAuthToken.as_view(), name='api_auth_logout'), # This maps the URL /api-auth/logout/ to the CustomAuthToken view
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'), # This maps the URL /api-token-auth/ to the CustomAuthToken view
    

>>>>>>> 13c8170 (worked on exception_al_urls, workshop_views.py)
]
