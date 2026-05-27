# Generated manually for Fase 3 validation updates.

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="empresa",
            name="codigo_pais",
            field=models.CharField(default="+51", max_length=6),
        ),
    ]
