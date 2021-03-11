from django.contrib import admin
from .models import MarcaVeiculo, Veiculo, Pessoa, Parametros, MovRotativo, Mensalista


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'total', 'horas_total')


admin.site.register(MarcaVeiculo)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)