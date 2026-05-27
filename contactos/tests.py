from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from empresas.models import Empresa

from .forms import ContactoForm
from .models import Contacto


class ContactoTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="analista",
            password="clave-segura-123",
        )
        self.empresa = Empresa.objects.create(
            razon_social="Empresa Demo S.A.C.",
            tipo_documento=Empresa.TipoDocumento.RUC,
            numero_documento="20600000001",
            correo="contacto@empresademo.local",
            codigo_pais="+51",
            telefono="064123456",
        )

    def login(self):
        self.client.login(username="analista", password="clave-segura-123")

    def build_contacto(self, **overrides):
        data = {
            "empresa": self.empresa,
            "nombres": "Juan Carlos",
            "apellidos": "Perez Ramos",
            "cargo": "Gerente de Operaciones",
            "correo": "juan.perez@empresademo.local",
            "codigo_pais_telefono": "+51",
            "telefono": "064123456",
            "codigo_pais_celular": "+51",
            "celular": "999888777",
            "es_principal": True,
            "notas": "Contacto de prueba para Fase 4.",
        }
        data.update(overrides)
        return Contacto.objects.create(**data)

    def test_contacto_str_uses_full_name_and_empresa(self):
        contacto = self.build_contacto()

        self.assertEqual(
            str(contacto),
            "Juan Carlos Perez Ramos - Empresa Demo S.A.C.",
        )

    def test_contacto_form_requires_empresa_and_nombres(self):
        form = ContactoForm(data={"correo": "juan.perez@empresademo.local"})

        self.assertFalse(form.is_valid())
        self.assertIn("empresa", form.errors)
        self.assertIn("nombres", form.errors)

    def test_contacto_rejects_email_without_domain_dot(self):
        contacto = self.build_contacto(correo="juan@empresa")

        with self.assertRaises(ValidationError) as error:
            contacto.full_clean()
        self.assertIn("correo", error.exception.message_dict)

    def test_contacto_phone_rejects_letters(self):
        contacto = self.build_contacto(telefono="064ABC456")

        with self.assertRaises(ValidationError) as error:
            contacto.full_clean()
        self.assertIn("telefono", error.exception.message_dict)

    def test_contacto_cellphone_requires_valid_length(self):
        contacto = self.build_contacto(celular="12345")

        with self.assertRaises(ValidationError) as error:
            contacto.full_clean()
        self.assertIn("celular", error.exception.message_dict)

    def test_contacto_list_requires_login(self):
        response = self.client.get(reverse("contactos:contacto_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_authenticated_user_can_create_contacto(self):
        self.login()

        response = self.client.post(
            reverse("contactos:contacto_create"),
            {
                "empresa": self.empresa.pk,
                "nombres": "Juan Carlos",
                "apellidos": "Perez Ramos",
                "cargo": "Gerente de Operaciones",
                "correo": "juan.perez@empresademo.local",
                "codigo_pais_telefono": "+51",
                "telefono": "064123456",
                "codigo_pais_celular": "+51",
                "celular": "999888777",
                "es_principal": "on",
                "notas": "Contacto de prueba para Fase 4.",
                "activo": "on",
            },
        )

        contacto = Contacto.objects.get(nombres="Juan Carlos")
        self.assertRedirects(
            response,
            reverse("contactos:contacto_detail", kwargs={"pk": contacto.pk}),
        )
        self.assertEqual(contacto.empresa, self.empresa)
        self.assertTrue(contacto.es_principal)

    def test_create_contacto_from_empresa_sets_empresa(self):
        self.login()

        response = self.client.post(
            reverse(
                "contactos:contacto_create_for_empresa",
                kwargs={"empresa_id": self.empresa.pk},
            ),
            {
                "empresa": self.empresa.pk,
                "nombres": "Maria",
                "apellidos": "Lopez",
                "correo": "maria.lopez@empresademo.local",
                "codigo_pais_telefono": "+51",
                "codigo_pais_celular": "+51",
                "activo": "on",
            },
        )

        contacto = Contacto.objects.get(nombres="Maria")
        self.assertRedirects(
            response,
            reverse("empresas:empresa_detail", kwargs={"pk": self.empresa.pk}),
        )
        self.assertEqual(contacto.empresa, self.empresa)

    def test_contacto_search_filters_by_name_role_phone_and_empresa(self):
        self.login()
        self.build_contacto()
        otra_empresa = Empresa.objects.create(
            razon_social="Otra Empresa S.A.C.",
            tipo_documento=Empresa.TipoDocumento.RUC,
            numero_documento="20600000002",
            codigo_pais="+51",
        )
        Contacto.objects.create(
            empresa=otra_empresa,
            nombres="Ana",
            apellidos="Silva",
            cargo="Compras",
        )

        search_terms = ["Juan", "Perez", "Gerente", "999888777", "Empresa Demo"]
        for term in search_terms:
            with self.subTest(term=term):
                response = self.client.get(reverse("contactos:contacto_list"), {"q": term})
                self.assertContains(response, "Juan Carlos")
                self.assertNotContains(response, "Ana")

    def test_contacto_can_be_updated(self):
        self.login()
        contacto = self.build_contacto()

        response = self.client.post(
            reverse("contactos:contacto_update", kwargs={"pk": contacto.pk}),
            {
                "empresa": self.empresa.pk,
                "nombres": "Juan Carlos",
                "apellidos": "Perez Ramos",
                "cargo": "Gerente General",
                "correo": "juan.perez@empresademo.local",
                "codigo_pais_telefono": "+51",
                "telefono": "064123456",
                "codigo_pais_celular": "+51",
                "celular": "999888777",
                "es_principal": "on",
                "notas": "Actualizado.",
                "activo": "on",
            },
        )

        contacto.refresh_from_db()
        self.assertRedirects(
            response,
            reverse("contactos:contacto_detail", kwargs={"pk": contacto.pk}),
        )
        self.assertEqual(contacto.cargo, "Gerente General")

    def test_contacto_deactivate_is_logical_and_requires_post(self):
        self.login()
        contacto = self.build_contacto()

        get_response = self.client.get(
            reverse("contactos:contacto_deactivate", kwargs={"pk": contacto.pk})
        )
        self.assertEqual(get_response.status_code, 405)

        response = self.client.post(
            reverse("contactos:contacto_deactivate", kwargs={"pk": contacto.pk})
        )

        contacto.refresh_from_db()
        self.assertRedirects(
            response,
            reverse("contactos:contacto_detail", kwargs={"pk": contacto.pk}),
        )
        self.assertFalse(contacto.activo)
        self.assertTrue(Contacto.objects.filter(pk=contacto.pk).exists())

    def test_empresa_detail_shows_associated_contacts(self):
        self.login()
        self.build_contacto()

        response = self.client.get(
            reverse("empresas:empresa_detail", kwargs={"pk": self.empresa.pk})
        )

        self.assertContains(response, "Contactos asociados")
        self.assertContains(response, "Juan Carlos")
        self.assertContains(response, "Principal")
