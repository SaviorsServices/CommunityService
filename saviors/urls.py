"""saviors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from saviors import views
from django.conf.urls import url
#from saviors.views import ServiceSearchListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('divulga/', include('divulga.urls')),    
    url(r'^$', views.index, name='index'),
    url(r'^list_search/', views.search_service_name, name='search_services'),
    url(r'^list_search_saude/', views.search_service_saude, name='search_services'),
    url(r'^list_search_educacional/', views.search_service_educacional, name='search_services'),
    url(r'^list_search_corte_de_cabelo/', views.search_service_corte, name='search_services'),
    url(r'^list_search_outra_categoria/', views.search_service_corte, name='search_services'),
]
