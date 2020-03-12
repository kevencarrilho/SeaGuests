from http.cookiejar import LWPCookieJar
from urllib.parse import urljoin

from requests import Session

from .forms import LeadForm, LoginForm
from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
# some_file.py

# Create your views here.
from . import models
from .models import Lead
dir()
from manager.models import Hostpot

UNIFI_SERVER = "https://unifi.seasolutions.com.br:8443/"
USERNAME = "external"
PASSWORD = "486279"
COOKIE_FILE = "/tmp/unifi_cookie"


def send_athorization(mac_id, minutes, site):
    login_url = urljoin(UNIFI_SERVER, "api/login")
    sesh = Session()
    sesh.cookies = LWPCookieJar(filename="test.cookies")
    sesh.cookies.save()
    #  login
    post_data = {
        "username": USERNAME,
        "password": PASSWORD}
    sesh.post(login_url, json=post_data)
    sesh.cookies.save()

    # post to api
    auth_url = urljoin(UNIFI_SERVER, 'api/s/' + site + '/cmd/stamgr')
    data = {'cmd': 'authorize-guest',
            'mac': mac_id,
            'minutes': minutes}
    sesh.post(auth_url, json=data)

    # logout
    logout_url = urljoin(UNIFI_SERVER, 'logout')
    sesh.post(logout_url)
    return True

# Create your views here.
def authenticate(request, site):

    mac = request.GET.get("id")
    ap = request.GET.get("ap")
    telefone = request.POST.get("telefone")
    if telefone:
        telefone = telefone.replace('(', '').replace(')', '').replace('-', '')
    # corrigir o get do lead
    lead= Lead.objects.filter(pk=telefone)

    hostpot = Hostpot.objects.filter(mac=ap, ativo=True)


    if  hostpot:
        for a in hostpot:
            hostpot = a
        form = LoginForm(request.POST)
        if lead:
            for a in lead:
                lead = a

            if form.is_valid():
                models.Session.objects.create(lead=lead,hostpot=hostpot)
                send_athorization(mac, 1, site)
                return redirect("https://www.google.com")

        else:
            form.add_error("telefone","Usuário não encontrado.")
            ap = request.GET.get("ap")
            id = request.GET.get("id")
            return render(request, "session/autenticar.html", {
                "form": form,
                "ap": ap,
                "id": id,
                "site": site,
                "erro": True
            }
                          )
    else:
        return render(request, "session/error.html", {"messagen": "Parece que o seu Hostpot não está registrado ou não foi ativo, procure o administrador da sua rede."})

def cadastrar(request, site):
    form = LeadForm()
    ap = request.GET.get("ap")
    id = request.GET.get("id")
    return render(request, "session/cadastro.html", {
                                              "form": form,
                                              "ap": ap,
                                              "id": id,
                                              "site": site
                                            }
                  )

def first(request, site):
    if(request.POST):
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        telefone = telefone.replace('(','').replace(')','').replace('-','')
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        if request.POST.get("sou_cliente"):
            sou_cliente = True
        else:
            sou_cliente = False
        models.Lead.objects.create(nome=nome, telefone=telefone, bairro=bairro, cidade=cidade, estado=estado,
        sou_cliente=sou_cliente)
    form = LoginForm(request.POST or None)
    ap = request.GET.get("ap")
    id = request.GET.get("id")
    return render(request, "session/autenticar.html", {
        "form": form,
        "ap": ap,
        "id": id,
        "site": site
    }
                  )