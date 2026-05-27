import re

from django.core.exceptions import ValidationError
from django.db import models


class Empresa(models.Model):
    class TipoDocumento(models.TextChoices):
        RUC = "RUC", "RUC"
        DNI = "DNI", "DNI"
        CE = "CE", "CE"
        OTRO = "OTRO", "Otro"

    class CodigoPais(models.TextChoices):
        PERU = "+51", "Peru (+51)"
        ARGENTINA = "+54", "Argentina (+54)"
        BOLIVIA = "+591", "Bolivia (+591)"
        BRASIL = "+55", "Brasil (+55)"
        CHILE = "+56", "Chile (+56)"
        COLOMBIA = "+57", "Colombia (+57)"
        COSTA_RICA = "+506", "Costa Rica (+506)"
        CUBA = "+53", "Cuba (+53)"
        ECUADOR = "+593", "Ecuador (+593)"
        EL_SALVADOR = "+503", "El Salvador (+503)"
        ESPANA = "+34", "Espana (+34)"
        ESTADOS_UNIDOS_CANADA = "+1", "Estados Unidos / Canada (+1)"
        GUATEMALA = "+502", "Guatemala (+502)"
        HONDURAS = "+504", "Honduras (+504)"
        MEXICO = "+52", "Mexico (+52)"
        NICARAGUA = "+505", "Nicaragua (+505)"
        PANAMA = "+507", "Panama (+507)"
        PARAGUAY = "+595", "Paraguay (+595)"
        URUGUAY = "+598", "Uruguay (+598)"
        VENEZUELA = "+58", "Venezuela (+58)"

    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=200, blank=True)
    tipo_documento = models.CharField(
        max_length=10,
        choices=TipoDocumento.choices,
        default=TipoDocumento.RUC,
    )
    numero_documento = models.CharField(max_length=30, unique=True)
    correo = models.EmailField(blank=True)
    codigo_pais = models.CharField(
        max_length=6,
        choices=CodigoPais.choices,
        default=CodigoPais.PERU,
    )
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.TextField(blank=True)
    sitio_web = models.URLField(blank=True)
    notas = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["razon_social"]
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.razon_social

    def clean(self):
        errors = {}

        numero_documento = (self.numero_documento or "").strip()
        self.numero_documento = numero_documento

        if numero_documento and not numero_documento.isdigit():
            errors["numero_documento"] = "El numero de documento solo debe contener digitos."
        elif self.tipo_documento == self.TipoDocumento.DNI and len(numero_documento) != 8:
            errors["numero_documento"] = "El DNI debe tener exactamente 8 digitos."
        elif self.tipo_documento == self.TipoDocumento.RUC and len(numero_documento) != 11:
            errors["numero_documento"] = "El RUC debe tener exactamente 11 digitos."
        elif self.tipo_documento == self.TipoDocumento.CE and len(numero_documento) != 9:
            errors["numero_documento"] = "El CE debe tener exactamente 9 digitos."

        correo = (self.correo or "").strip()
        self.correo = correo
        if correo and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
            errors["correo"] = "Ingresa un correo valido con dominio, por ejemplo usuario@dominio.com."

        codigo_pais = (self.codigo_pais or "").strip()
        self.codigo_pais = codigo_pais
        codigos_validos = {choice.value for choice in self.CodigoPais}
        if codigo_pais and codigo_pais not in codigos_validos:
            errors["codigo_pais"] = "Selecciona un codigo de pais valido."

        telefono = (self.telefono or "").strip()
        self.telefono = telefono
        if telefono:
            if not telefono.isdigit():
                errors["telefono"] = "El telefono solo debe contener digitos."
            elif len(telefono) < 6 or len(telefono) > 15:
                errors["telefono"] = "El telefono debe tener entre 6 y 15 digitos."

        if errors:
            raise ValidationError(errors)
