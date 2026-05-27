# Generated manually for Fase 4.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("empresas", "0003_alter_empresa_codigo_pais_choices"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombres", models.CharField(max_length=120)),
                ("apellidos", models.CharField(blank=True, max_length=120)),
                ("cargo", models.CharField(blank=True, max_length=120)),
                ("correo", models.EmailField(blank=True, max_length=254)),
                ("telefono", models.CharField(blank=True, max_length=50)),
                ("celular", models.CharField(blank=True, max_length=50)),
                ("es_principal", models.BooleanField(default=False)),
                ("notas", models.TextField(blank=True)),
                ("activo", models.BooleanField(default=True)),
                ("creado_en", models.DateTimeField(auto_now_add=True)),
                ("actualizado_en", models.DateTimeField(auto_now=True)),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contactos",
                        to="empresas.empresa",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contacto",
                "verbose_name_plural": "Contactos",
                "ordering": ["empresa", "apellidos", "nombres"],
            },
        ),
    ]
