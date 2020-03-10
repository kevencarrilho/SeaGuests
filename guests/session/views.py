from http.cookiejar import LWPCookieJar
from urllib.parse import urljoin

from requests import Session

from .forms import LeadForm, SessionForm, LoginForm
from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from . import models

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
    telefone = "+55" + telefone.replace('(', '').replace(')', '').replace('-', '')
    # corrigir o get do lead
    lead= get_object_or_404(models.Lead,pk=telefone)
    hostpot = get_object_or_404(models.Hostpot,pk=ap)
    if  hostpot != None:
        session = models.Session.objects.create(nome=hostpot.nome,lead=lead)
            # (None).save(commit=False)
        # session.name = hostpot.nome
        # session.lead = lead
        # session.save()
        send_athorization(mac, 1, site)
        return redirect("https://www.google.com")


def cadastrar(request, site):
    form = LeadForm()
    ap = request.GET.get("ap")
    id = request.GET.get("id")
    return render(request, "cadastro.html", {
                                              "form": form,
                                              "ap": ap,
                                              "id": id,
                                              "site": site
                                            }
                  )

def index(request, site):
    if(request.POST):
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        telefone = "+55" + telefone.replace('(','').replace(')','').replace('-','')
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        models.Lead.objects.create(nome=nome, telefone=telefone, bairro=bairro, cidade=cidade)
    form = LoginForm(request.POST or None)
    ap = request.GET.get("ap")
    id = request.GET.get("id")
    return render(request, "autenticar.html", {
        "form": form,
        "ap": ap,
        "id": id,
        "site": site
    }
                  )