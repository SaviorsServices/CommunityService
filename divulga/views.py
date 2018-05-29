from django.shortcuts import get_object_or_404
from django.shortcuts import render
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Divulgacoes
import requests
from django.contrib.auth.decorators import login_required
from .forms import CommunityActionForm, DonationForm, HealthServiceForm, EstablishmentForm 
from .models import Establishment, HealthService, Donation

@login_required
def formevent(request):
    if request.method == 'POST':
        divulgacao = Divulgacoes()
        divulgacao.nomeEvento = request.POST['nomeEvento']
        divulgacao.categoria = request.POST['categoria']
        divulgacao.cidade = request.POST['cidade']
        #divulgacao.bairro = request.POST['bairro']
        divulgacao.endereco = request.POST['endereco']
        #divulgacao.cep = request.POST['cep']
        divulgacao.telefone = request.POST['telefone']
        divulgacao.horarioInicio = request.POST['horarioInicio']
        divulgacao.horarioFim = request.POST['horarioFim']
        divulgacao.data = request.POST['data']
        divulgacao.user = request.user
        divulgacao.save()
        return render(request , 'index.html')
    return render(request , 'formevent.html')

def mapa(request, id):
    latitude = 0
    longitude = 0
    if request.method == "POST":
        chave = "AIzaSyDroa8JCUm2JfRZ_7eVMb4Fqx8ufr0Mz_A"
        div = Establishment.objects.get(id=id)
        address = div.endereco+"+"+div.cidade
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+chave)
        if r.status_code == 200:
            dados = json.loads(r.content)
            latitude = dados["results"][0]["geometry"]["location"]["lat"]
            longitude = dados["results"][0]["geometry"]["location"]["lng"]
            #print(latitude)
            #print(longitude)
        return render(request, 'mapa.html', {'latitude':latitude, 'longitude': longitude})
    return render(request, 'index.html')



def servicolist(request):
    div = Divulgacoes.objects.all()
    return render(request, 'servicolist.html', {'div':div})


def create_establishment(request):
    title = "Cadastrar Estabelecimento"
    if request.method == "POST":
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = EstablishmentForm()
        return render(request, 'establishment.html', {'form': form,'title':title})


from .forms import CommunityActionForm, DonationForm, HealthServiceForm, EstablishmentForm 
    
def create_health_service(request):
    title = "Cadastrar Serviço de Saude"
    if request.method == "POST":
        form = HealthServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = HealthServiceForm()
        return render(request, 'establishment.html', {'form': form,'title':title})

def create_donation(request):
    title = "Cadastrar Doação"
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request, 'establishment.html', {'form': form,'title':title})

    else:
        form = DonationForm()
        return render(request, 'establishment.html', {'form': form,'title':title})

def edit_establishment(request, id):
    title = "Editar Estabelecimento"
    establishment = get_object_or_404(Establishment, id=id)
    if request.method == "POST":
        form = EstablishmentForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'establishment.html', {'form': form,'title':title})
    else:
        form = EstablishmentForm(instance=establishment)
        return render(request, 'establishment.html', {'form': form,'title':title})

def edit_health_service(request, id):
    title = "Editar Serviço de Saude"
    health_service = get_object_or_404(HealthService, id=id)
    if request.method == "POST":
        form = HealthServiceForm(request.POST, instance=health_service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'establishment.html', {'form': form,'title':title})
    else:
        form = HealthServiceForm(instance=health_service)
        return render(request, 'establishment.html', {'form': form,'title':title})


def edit_donation(request, id):
    title = "Editar Doação"
    donation = get_object_or_404(Donation, id=id)
    if request.method == "POST":
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'establishment.html', {'form': form,'title':title})
    else:
        form = DonationForm(instance=donation)
        return render(request, 'establishment.html', {'form': form,'title':title})


def delete_establishment(request, id):
    establishment = get_object_or_404(Establishment, id=id)
    establishment.delete()
    return render(request, 'delete.html')

def delete_health_service(request, id):
    health_service = get_object_or_404(HealthService, id=id)
    health_service.delete()
    return render(request, 'delete.html')

def delete_donation(request, id):
    delete_donation = get_object_or_404(Donation, id=id)
    delete_donation.delete()
    return render(request, 'delete.html')

def list_establishment(request):
    establishments = Establishment.objects.all()
    print(establishments)
    return render(request, 'list_establishment.html', {"establishments": establishments})

def list_health_service(request):
    health_services = HealthService.objects.all() 
    return render(request, 'list_health_service.html', {"health_services": health_services})

def list_donation(request):
    donations = Donation.objects.all()
    return render(request, 'list_donation.html', {"donations": donations})
