from django.contrib import admin

from .models import Contacto


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_completo",
        "empresa",
        "cargo",
        "correo",
        "codigo_pais_telefono",
        "telefono",
        "codigo_pais_celular",
        "celular",
        "es_principal",
        "activo",
        "creado_en",
    )
    list_filter = ("activo", "es_principal", "empresa", "creado_en")
    search_fields = (
        "nombres",
        "apellidos",
        "cargo",
        "correo",
        "telefono",
        "celular",
        "empresa__razon_social",
        "empresa__nombre_comercial",
    )
    readonly_fields = ("creado_en", "actualizado_en")
