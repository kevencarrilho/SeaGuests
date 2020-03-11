from django.db import models

# Create your models here.

class Hostpot(models.Model):
    nome = models.CharField(max_length=60, primary_key=True)
    mac = models.CharField(max_length=60)
    rua = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=60,choices=(("ac","AC"), ("al","AL"), ("ap","AP"), ("am","AM"),
                                                    ("ba","BA"), ("ce","CE"), ("df","DF"), ("es","ES"),
                                                    ("go","GO"), ("ma","MA"), ("mt","MT"), ("ms","MS"),
                                                    ("mg","MG"), ("pa","PA"), ("pb","PB"), ("pr","PR"),
                                                    ("pe","PE"), ("pi","PI"), ("rj","RJ"), ("rn","RN"),
                                                    ("rs","RS"), ("ro","RO"), ("rr","RR"), ("sc","SC"),
                                                    ("sp","SP"), ("se","SE")),default='pa')
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome