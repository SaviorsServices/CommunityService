from django.shortcuts import render, redirect
from divulga.models import CommunityAction
from django.db.models import Q
import operator
from django.views.generic.base import View

def index(request):
    return render(request, 'index.html')

#Buscar por nome
def search_service_name(request):
    services_list_name = CommunityAction.objects.all()
    query = request.GET.get("q")
    
    services_list_name = services_list_name.filter(name__icontains=query)
    return render(request, 'list_search.html', {"services_list": services_list_name})
    #href="{% url 'search_services' %}"

#Tags categoria index
def search_service_saude(request):
    services_list_category = CommunityAction.objects.all()
    categoria = 'SAUDE'
    services_list_category = services_list_category.filter(category__icontains=categoria)
    return render(request, 'list_search.html', {"services_list": services_list_category})

def search_service_educacional(request):
    services_list_category = CommunityAction.objects.all()
    categoria = 'EDUCACIONAL'
    services_list_category = services_list_category.filter(category__icontains=categoria)
    return render(request, 'list_search.html', {"services_list": services_list_category})

def search_service_corte(request):
    services_list_corte = CommunityAction.objects.all()
    categoria = 'CORTE DE CABELO'
    services_list_corte = services_list_corte.filter(category__icontains=categoria)
    return render(request, 'list_search.html', {"services_list": services_list_corte})

def search_service_outra_categoria(request):
    services_list_outra_categoria = CommunityAction.objects.all()
    categoria = 'OUTRA CATEGORIA'
    services_list_outra_categoria = services_list_outra_categoria.filter(category__icontains=categoria)
    return render(request, 'list_search.html', {"services_list": services_list_outra_categoria})


