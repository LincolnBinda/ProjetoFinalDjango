from django.db import models


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