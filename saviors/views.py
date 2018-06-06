from django.shortcuts import render
from divulga.models import CommunityAction
from django.db.models import Q


def index(request):
    return render(request, 'index.html')

def search_service(request):
    services_list = CommunityAction.objects.all()
    query = request.GET.get("q")
    
    services_list = services_list.filter(name__icontains=query)
    print(services_list)
    print("ue")
    return render(request, 'list_search.html', {"services_list": services_list})
    #href="{% url 'search_services' %}"

