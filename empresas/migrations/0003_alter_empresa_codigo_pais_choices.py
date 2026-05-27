# Generated manually to make country codes selectable.

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresas", "0002_empresa_codigo_pais"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="codigo_pais",
            field=models.CharField(
                choices=[
                    ("+51", "Peru (+51)"),
                    ("+54", "Argentina (+54)"),
                    ("+591", "Bolivia (+591)"),
                    ("+55", "Brasil (+55)"),
                    ("+56", "Chile (+56)"),
                    ("+57", "Colombia (+57)"),
                    ("+506", "Costa Rica (+506)"),
                    ("+53", "Cuba (+53)"),
                    ("+593", "Ecuador (+593)"),
                    ("+503", "El Salvador (+503)"),
                    ("+34", "Espana (+34)"),
                    ("+1", "Estados Unidos / Canada (+1)"),
                    ("+502", "Guatemala (+502)"),
                    ("+504", "Honduras (+504)"),
                    ("+52", "Mexico (+52)"),
                    ("+505", "Nicaragua (+505)"),
                    ("+507", "Panama (+507)"),
                    ("+595", "Paraguay (+595)"),
                    ("+598", "Uruguay (+598)"),
                    ("+58", "Venezuela (+58)"),
                ],
                default="+51",
                max_length=6,
            ),
        ),
    ]
