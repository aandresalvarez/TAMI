from django.contrib import admin

# Register your models here.
from nucleo.models import Enfermedad,Madre,Lote,Marcador,Neonato,Valor_marcadores_de_cada_neonato


admin.site.register(Enfermedad)
admin.site.register(Madre)
admin.site.register(Lote)
admin.site.register(Marcador)
admin.site.register(Neonato)
admin.site.register(Valor_marcadores_de_cada_neonato)