# Create your models here.

from django.db import models

class Lead(models.Model):
    nome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=14, primary_key=True)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=2,choices=(("ac","AC"), ("al","AL"), ("ap","AP"), ("am","AM"),
                                                    ("ba","BA"), ("ce","CE"), ("df","DF"), ("es","ES"),
                                                    ("go","GO"), ("ma","MA"), ("mt","MT"), ("ms","MS"),
                                                    ("mg","MG"), ("pa","PA"), ("pb","PB"), ("pr","PR"),
                                                    ("pe","PE"), ("pi","PI"), ("rj","RJ"), ("rn","RN"),
                                                    ("rs","RS"), ("ro","RO"), ("rr","RR"), ("sc","SC"),
                                                    ("sp","SP"), ("se","SE")),default='pa')
    sou_cliente = models.BooleanField(default=False)
    def __str__(self):
        return self.nome

class Session(models.Model):
    lead = models.ForeignKey("Lead", on_delete=models.CASCADE, related_name='lead')
    hostpot = models.ForeignKey("manager.Hostpot", on_delete=models.CASCADE, related_name='hostpot')
    def __str__(self):
        return "Cliente: " + self.lead.nome + " Parceiro: " + self.hostpot.nome


