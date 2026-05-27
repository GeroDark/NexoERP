from django.contrib import admin

from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "razon_social",
        "nombre_comercial",
        "tipo_documento",
        "numero_documento",
        "correo",
        "codigo_pais",
        "telefono",
        "activo",
        "creado_en",
    )
    list_filter = ("activo", "tipo_documento", "creado_en")
    search_fields = (
        "razon_social",
        "nombre_comercial",
        "numero_documento",
        "correo",
    )
    readonly_fields = ("creado_en", "actualizado_en")
