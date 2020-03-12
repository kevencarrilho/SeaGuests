from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .forms import HostpotForm
from .models import Hostpot


@login_required
def index(request):
    nome = request.GET.get("nome")
    if nome:
        hostpots = Hostpot.objects.filter(nome__icontains =nome )
    else:
        hostpots = Hostpot.objects.all()
    return render(request, "manager/main.html", {"hostpot": hostpots})

@login_required
def new(request):
    form = HostpotForm()
    return render(request, "manager/form.html", {"form": form})

@login_required
def edit(request, nome):
    hostpots = Hostpot.objects.filter(nome=nome).first()
    form = HostpotForm(request.POST or None, instance=hostpots)
    return render(request, "manager/form.html", {"form": form})

@login_required
def save(request):
    if request.POST.get("ativo"):
        ativo = True
    else:
        ativo = False
    obj, created = Hostpot.objects.update_or_create(
        nome=request.POST.get("nome"),
        defaults={
        "nome": request.POST.get("nome"),
        "endereco_mac": request.POST.get("endereco_mac").replace(':', ''),
        "rua": request.POST.get("rua"),
        "bairro": request.POST.get("bairro"),
        "cidade": request.POST.get("cidade"),
        "estado": request.POST.get("estado"),
        "ativo": ativo}
    )
    return redirect("index")
