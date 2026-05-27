from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import EmpresaForm
from .models import Empresa


@login_required
def empresa_list(request):
    query = request.GET.get("q", "").strip()
    empresas = Empresa.objects.all()

    if query:
        empresas = empresas.filter(
            Q(razon_social__icontains=query)
            | Q(nombre_comercial__icontains=query)
            | Q(numero_documento__icontains=query)
            | Q(correo__icontains=query)
        )

    return render(
        request,
        "empresas/empresa_list.html",
        {
            "empresas": empresas,
            "query": query,
        },
    )


@login_required
def empresa_create(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            messages.success(request, "Empresa creada correctamente.")
            return redirect("empresas:empresa_detail", pk=empresa.pk)
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = EmpresaForm()

    return render(
        request,
        "empresas/empresa_form.html",
        {
            "form": form,
            "title": "Nueva empresa",
            "submit_label": "Crear empresa",
        },
    )


@login_required
def empresa_detail(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, "empresas/empresa_detail.html", {"empresa": empresa})


@login_required
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)

    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            empresa = form.save()
            messages.success(request, "Empresa actualizada correctamente.")
            return redirect("empresas:empresa_detail", pk=empresa.pk)
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = EmpresaForm(instance=empresa)

    return render(
        request,
        "empresas/empresa_form.html",
        {
            "form": form,
            "empresa": empresa,
            "title": "Editar empresa",
            "submit_label": "Guardar cambios",
        },
    )


@login_required
@require_POST
def empresa_deactivate(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)

    if empresa.activo:
        empresa.activo = False
        empresa.save(update_fields=["activo", "actualizado_en"])
        messages.success(request, "Empresa desactivada correctamente.")
    else:
        messages.info(request, "La empresa ya estaba inactiva.")

    return redirect("empresas:empresa_detail", pk=empresa.pk)
