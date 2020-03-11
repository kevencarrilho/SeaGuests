from django import forms

from .models import Lead, Session


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["nome", "telefone", "bairro", "cidade", "estado"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["telefone"]

