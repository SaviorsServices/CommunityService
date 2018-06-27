from django.shortcuts import render, redirect
from divulga.models import CommunityAction, HealthService, Establishment, Donation
from django.db.models import Q
import operator
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html')


# Buscar por nome
def search_service_name(request):
    services_list_name = CommunityAction.objects.all()
    query = request.GET.get("q")
    services_list_name = services_list_name.filter(name__icontains=query)
    name = "Serviços"

    return render(
        request,
        'list_search.html',
        {"services_list": services_list_name, "name": name}
        )


# Tags categoria index
def search_service_saude(request):
    services_list_category = CommunityAction.objects.all()
    categoria = 'SAUDE'
    services_list_category = services_list_category.filter(
                                category__icontains=categoria
                                )
    name = "Serviços de Saúde"

    return render(
        request,
        'list_search.html',
        {"services_list": services_list_category, "name": name}
        )


def search_service_educacional(request):

    services_list_category = CommunityAction.objects.all()
    categoria = 'EDUCACIONAL'
    services_list_category = services_list_category.filter(
                                category__icontains=categoria
                                )
    name = "Serviços educacionais"

    return render(
        request,
        'list_search.html',
        {"services_list": services_list_category, "name": name}
        )


def search_service_corte(request):
    services_list_corte = CommunityAction.objects.all()
    categoria = 'CORTE DE CABELO'
    services_list_corte = services_list_corte.filter(
                            category__icontains=categoria
                            )
    name = "Serviços"

    return render(
        request,
        'list_search.html',
        {"services_list": services_list_corte, "name": name}
        )


def search_service_outra_categoria(request):
    services_list_outra_categoria = CommunityAction.objects.all()
    categoria = 'OUTRA CATEGORIA'
    services_list_outra_categoria = services_list_outra_categoria.filter(
                                        category__icontains=categoria
                                        )
    name = "Serviços"

    return render(
        request,
        'list_search.html',
        {"services_list": services_list_outra_categoria, "name": name}
        )


def list_all_services(request):
    services_list_name = HealthService.objects.all()

    # services_list_name = services_list_name.filter(name__icontains=query)
    name = "Serviços de Saúde"
    return render(
        request,
        'list_search.html',
        {"services_list": services_list_name, "name": name}
        )


def list_all_donations(request):
    services_list_name = Donation.objects.all()
    name = "Doações"
    return render(
        request,
        'list_search.html',
        {"services_list": services_list_name, "name": name}
        )


def list_all_establishment(request):
    services_list_name = Establishment.objects.all()
    name = "Estabelecimentos"
    return render(
        request,
        'list_search.html',
        {"services_list": services_list_name, "name": name}
        )
