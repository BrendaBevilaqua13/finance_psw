from django.contrib import admin
from .models import Conta, Categoria

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ['apelido','banco','tipo','valor']
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria','essencial','valor_planejamento']