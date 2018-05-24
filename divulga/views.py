from django.shortcuts import render
from .models import Divulgacoes
from django.contrib.auth.decorators import login_required

@login_required
def formevent(request):
    if request.method == 'POST':
        divulgacao = Divulgacoes()
        divulgacao.nomeEvento = request.POST['nomeEvento']
        divulgacao.cidade = request.POST['cidade']
        divulgacao.bairro = request.POST['bairro']
        divulgacao.endereco = request.POST['endereco']
        divulgacao.cep = request.POST['cep']
        divulgacao.telefone = request.POST['telefone']
        divulgacao.user = request.user
        divulgacao.save()
    return render(request , 'formevent.html')