from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create base role groups for NexoERP."

    def handle(self, *args, **options):
        role_names = [
            "Administrador",
            "Gerencia",
            "Analista",
            "Invitado",
        ]

        for role_name in role_names:
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Grupo creado: {group.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Grupo existente: {group.name}"))
