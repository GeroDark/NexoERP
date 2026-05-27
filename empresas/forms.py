from django import forms

from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "razon_social",
            "nombre_comercial",
            "tipo_documento",
            "numero_documento",
            "correo",
            "codigo_pais",
            "telefono",
            "direccion",
            "sitio_web",
            "notas",
            "activo",
        ]
        widgets = {
            "direccion": forms.Textarea(attrs={"rows": 3}),
            "notas": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(field.widget, forms.Select):
                css_class = "form-select"
            else:
                css_class = "form-control"
            field.widget.attrs["class"] = css_class
