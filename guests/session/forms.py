from django import forms
from django.db.models import QuerySet

from .models import Lead, Session


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["nome", "telefone", "bairro", "cidade", "estado"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["telefone"]

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ["nome", "lead"]
