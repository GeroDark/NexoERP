from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Empresa


class EmpresaValidationTests(TestCase):
    def build_empresa(self, **overrides):
        data = {
            "razon_social": "Empresa Demo S.A.C.",
            "tipo_documento": Empresa.TipoDocumento.RUC,
            "numero_documento": "20600000001",
            "correo": "contacto@empresademo.local",
            "codigo_pais": "+51",
            "telefono": "999999999",
        }
        data.update(overrides)
        return Empresa(**data)

    def test_ruc_requires_11_digits(self):
        empresa = self.build_empresa(numero_documento="2060000000")

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("numero_documento", error.exception.message_dict)

    def test_dni_requires_8_digits(self):
        empresa = self.build_empresa(
            tipo_documento=Empresa.TipoDocumento.DNI,
            numero_documento="12345678",
        )

        empresa.full_clean()

    def test_ce_requires_9_digits(self):
        empresa = self.build_empresa(
            tipo_documento=Empresa.TipoDocumento.CE,
            numero_documento="123456789",
        )

        empresa.full_clean()

    def test_otro_allows_variable_digits_only(self):
        empresa = self.build_empresa(
            tipo_documento=Empresa.TipoDocumento.OTRO,
            numero_documento="123456",
        )

        empresa.full_clean()

    def test_document_number_rejects_letters(self):
        empresa = self.build_empresa(
            tipo_documento=Empresa.TipoDocumento.OTRO,
            numero_documento="ABC123",
        )

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("numero_documento", error.exception.message_dict)

    def test_email_requires_domain_with_dot(self):
        empresa = self.build_empresa(correo="contacto@empresa")

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("correo", error.exception.message_dict)

    def test_country_code_must_be_selected_from_choices(self):
        empresa = self.build_empresa(codigo_pais="+999")

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("codigo_pais", error.exception.message_dict)

    def test_country_code_accepts_configured_choice(self):
        empresa = self.build_empresa(codigo_pais="+57")

        empresa.full_clean()

    def test_phone_rejects_letters(self):
        empresa = self.build_empresa(telefono="999ABC999")

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("telefono", error.exception.message_dict)

    def test_phone_requires_valid_length(self):
        empresa = self.build_empresa(telefono="12345")

        with self.assertRaises(ValidationError) as error:
            empresa.full_clean()

        self.assertIn("telefono", error.exception.message_dict)
