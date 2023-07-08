from django.contrib import admin
from .models import Valores

# Register your models here.
@admin.register
class ValoresAdmin(admin.ModelAdmin):
    list_display = ['valor', 'tipo', 'conta', 'categoria', 'data']