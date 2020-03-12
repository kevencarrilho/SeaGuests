from django import forms

from .models import Hostpot


class HostpotForm(forms.ModelForm):

    class Meta:
        model = Hostpot
        fields = ["nome", "endereco_mac", "rua", "bairro", "cidade", "estado", "ativo"]



