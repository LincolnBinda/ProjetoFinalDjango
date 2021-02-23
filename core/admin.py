from django.contrib import admin
from .models import MarcaVeiculo, Veiculo, Pessoa, Parametros


admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)