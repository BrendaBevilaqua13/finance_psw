from django.contrib import admin
from . models import ContaPaga, ContaPagar

# Register your models here.
@admin.register(ContaPagar)
class ContaPagarAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'valor', 'dia_pagamento']
    
@admin.register(ContaPaga)
class ContaPagaAdmin(admin.ModelAdmin):
    list_display = ['conta', 'data_pagamento']
