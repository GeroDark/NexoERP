from django import forms

from empresas.models import Empresa

from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
            "empresa",
            "nombres",
            "apellidos",
            "cargo",
            "correo",
            "codigo_pais_telefono",
            "telefono",
            "codigo_pais_celular",
            "celular",
            "es_principal",
            "notas",
            "activo",
        ]
        widgets = {
            "notas": forms.Textarea(attrs={"rows": 4}),
        }
        labels = {
            "codigo_pais_telefono": "Codigo de pais (telefono)",
            "codigo_pais_celular": "Codigo de pais (celular)",
        }

    def __init__(self, *args, empresa=None, empresa_locked=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.empresa_locked = empresa_locked

        self.fields["empresa"].queryset = Empresa.objects.order_by("razon_social")
        if empresa is not None:
            self.fields["empresa"].initial = empresa

        if empresa_locked:
            self.fields["empresa"].queryset = Empresa.objects.filter(pk=empresa.pk)
            self.fields["empresa"].widget = forms.HiddenInput()

        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(field.widget, forms.Select):
                css_class = "form-select"
            elif isinstance(field.widget, forms.HiddenInput):
                continue
            else:
                css_class = "form-control"
            field.widget.attrs["class"] = css_class
