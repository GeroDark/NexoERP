# Generated manually for Fase 4 contact phone country codes.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contactos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contacto",
            name="codigo_pais_telefono",
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
        migrations.AddField(
            model_name="contacto",
            name="codigo_pais_celular",
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
