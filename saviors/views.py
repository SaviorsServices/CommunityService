from django.shortcuts import render, redirect
from divulga.models import CommunityAction
from django.db.models import Q
import operator
from django.views.generic.base import View

def index(request):
    return render(request, 'index.html')

def search_service_name(request):
    services_list_name = CommunityAction.objects.all()
    query = request.GET.get("q")
    
    services_list_name = services_list_name.filter(name__icontains=query)
    print(services_list_name)
    print("ue")
    return render(request, 'list_search.html', {"services_list": services_list_name})
    #href="{% url 'search_services' %}"

def search_service_category(request):
    services_list_category = CommunityAction.objects.all()
    categoria = 'SAUDE'
    services_list_category = services_list_category.filter(category__icontains=categoria)
    print(services_list_category)
    print("ue")
    return render(request, 'list_search.html', {"services_list": services_list_category})
    #return redirect('search_services')
    #href="{% url 'search_services' %}"

