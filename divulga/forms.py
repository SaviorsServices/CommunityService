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

        self.helper.add_input(Submit('submit', 'Submit'))


    class Meta:
        model = Donation
        fields = '__all__'

class HealthServiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealthServiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))



    class Meta:
        model = HealthService
        fields = '__all__'

class EstablishmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstablishmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Establishment
        fields = '__all__'
