from django import forms

from guests.manager.models import Hostpot


class HostpotForm(forms.ModelForm):
    class Meta:
        model = Hostpot
        fields = ["nome", "mac", "rua", "bairro", "cidade", "estado", "ativo"]



