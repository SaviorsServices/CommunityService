from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CommunityAction, Donation, HealthService, Establishment

class CommunityActionForm(ModelForm):
    class Meta:
        model = CommunityAction
        fields = '__all__'


class DonationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Enviar'))


    class Meta:
        model = Donation

        fields = '__all__'
        labels = {
            'name': 'Nome',
            'start_date': 'Data de Inicio', 
            'close_date': 'Data de Encerramento',
            'description': 'Descrição', 
            'establishment': 'Estabelecimento',
            'start_hour': 'Horario de Inicio',
            'close_hour': 'Horario de Fechamento'
        }

        widgets = {
            'start_date': forms.DateInput(format="%d/%m/%Y"),
            'close_date': forms.DateInput(format="%d/%m/%Y")
        }

        start_date = forms.DateField(input_formats="%d/%m/%Y")
         
class HealthServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealthServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Enviar'))



    class Meta:
        model = HealthService
        start_date = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))
        close_date = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'start_date': 'Data de Inicio', 
            'close_date': 'Data de Encerramento',
            'description': 'Descrição', 
            'establishment': 'Estabelecimento',
            'item_name': 'Nome do Item ',
            'amount': 'Quantidade'
        }
        widgets = {
            'start_date': forms.widgets.DateInput(format="%d/%m/%Y"),
            'close_date': forms.widgets.DateInput(format="%d/%m/%Y")
        }

        
class EstablishmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstablishmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Enviar'))

    class Meta:
        model = Establishment
        fields = '__all__'
        labels = {
            'name': 'nome',
            'openHour': 'Horario de Abertura',
            'closeHour': 'Horario de Fechamento',
            'telefone': 'Telefone',
            'cidade': 'Cidade',
            'bairro': 'Bairro',
            'endereco': 'Endereço',
            'cep': 'cep'
        }
