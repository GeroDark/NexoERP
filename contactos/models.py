from django.core.exceptions import ValidationError
from django.db import models

from empresas.models import Empresa


class Contacto(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="contactos",
    )
    nombres = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120, blank=True)
    cargo = models.CharField(max_length=120, blank=True)
    correo = models.EmailField(blank=True)
    codigo_pais_telefono = models.CharField(
        max_length=6,
        choices=Empresa.CodigoPais.choices,
        default=Empresa.CodigoPais.PERU,
    )
    telefono = models.CharField(max_length=50, blank=True)
    codigo_pais_celular = models.CharField(
        max_length=6,
        choices=Empresa.CodigoPais.choices,
        default=Empresa.CodigoPais.PERU,
    )
    celular = models.CharField(max_length=50, blank=True)
    es_principal = models.BooleanField(default=False)
    notas = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["empresa", "apellidos", "nombres"]
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.nombre_completo} - {self.empresa}"

    @property
    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}".strip()

    def clean(self):
        errors = {}

        correo = (self.correo or "").strip()
        self.correo = correo
        if correo and "." not in correo.rsplit("@", 1)[-1]:
            errors["correo"] = "Ingresa un correo valido con dominio, por ejemplo usuario@dominio.com."

        codigos_validos = {choice.value for choice in Empresa.CodigoPais}
        for field_name in ["codigo_pais_telefono", "codigo_pais_celular"]:
            codigo = (getattr(self, field_name) or "").strip()
            setattr(self, field_name, codigo)
            if codigo and codigo not in codigos_validos:
                errors[field_name] = "Selecciona un codigo de pais valido."

        for field_name, label in [("telefono", "telefono"), ("celular", "celular")]:
            numero = (getattr(self, field_name) or "").strip()
            setattr(self, field_name, numero)
            if numero:
                if not numero.isdigit():
                    errors[field_name] = f"El {label} solo debe contener digitos."
                elif len(numero) < 6 or len(numero) > 15:
                    errors[field_name] = f"El {label} debe tener entre 6 y 15 digitos."

        if errors:
            raise ValidationError(errors)
