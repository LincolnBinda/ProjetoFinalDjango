from django.db import models
from datetime import datetime
import math


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class MarcaVeiculo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(MarcaVeiculo, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=E1101
        #return self.marca.__str__() + ' - ' + self.placa
        return self.marca.nome + ' - ' + self.placa

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'

class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    def __str__(self):
        # pylint: disable=E1101
        return self.veiculo.placa

    def total(self):
        return self.valor_hora * self.horas_total()

    def horas_total(self):
        if self.checkout is None:
            return math.ceil((self.checkin - self.checkin).total_seconds() / 3600)
        else:
            return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.valor_mes)

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)