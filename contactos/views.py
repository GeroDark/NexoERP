from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from empresas.models import Empresa

from .forms import ContactoForm
from .models import Contacto


@login_required
def contacto_list(request):
    query = request.GET.get("q", "").strip()
    contactos = Contacto.objects.select_related("empresa").all()

    if query:
        contactos = contactos.filter(
            Q(nombres__icontains=query)
            | Q(apellidos__icontains=query)
            | Q(cargo__icontains=query)
            | Q(correo__icontains=query)
            | Q(codigo_pais_telefono__icontains=query)
            | Q(telefono__icontains=query)
            | Q(codigo_pais_celular__icontains=query)
            | Q(celular__icontains=query)
            | Q(empresa__razon_social__icontains=query)
            | Q(empresa__nombre_comercial__icontains=query)
        )

    return render(
        request,
        "contactos/contacto_list.html",
        {
            "contactos": contactos,
            "query": query,
        },
    )


@login_required
def contacto_create(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            messages.success(request, "Contacto creado correctamente.")
            return redirect("contactos:contacto_detail", pk=contacto.pk)
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ContactoForm()

    return render(
        request,
        "contactos/contacto_form.html",
        {
            "form": form,
            "title": "Nuevo contacto",
            "submit_label": "Crear contacto",
        },
    )


@login_required
def contacto_create_for_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    if request.method == "POST":
        form = ContactoForm(request.POST, empresa=empresa, empresa_locked=True)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.empresa = empresa
            contacto.save()
            messages.success(request, "Contacto creado correctamente.")
            return redirect("empresas:empresa_detail", pk=empresa.pk)
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ContactoForm(empresa=empresa, empresa_locked=True)

    return render(
        request,
        "contactos/contacto_form.html",
        {
            "form": form,
            "empresa": empresa,
            "title": "Nuevo contacto",
            "submit_label": "Crear contacto",
        },
    )


@login_required
def contacto_detail(request, pk):
    contacto = get_object_or_404(Contacto.objects.select_related("empresa"), pk=pk)
    return render(request, "contactos/contacto_detail.html", {"contacto": contacto})


@login_required
def contacto_update(request, pk):
    contacto = get_object_or_404(Contacto.objects.select_related("empresa"), pk=pk)

    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            contacto = form.save()
            messages.success(request, "Contacto actualizado correctamente.")
            return redirect("contactos:contacto_detail", pk=contacto.pk)
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ContactoForm(instance=contacto)

    return render(
        request,
        "contactos/contacto_form.html",
        {
            "form": form,
            "contacto": contacto,
            "title": "Editar contacto",
            "submit_label": "Guardar cambios",
        },
    )


@login_required
@require_POST
def contacto_deactivate(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)

    if contacto.activo:
        contacto.activo = False
        contacto.save(update_fields=["activo", "actualizado_en"])
        messages.success(request, "Contacto desactivado correctamente.")
    else:
        messages.info(request, "El contacto ya estaba inactivo.")

    next_url = request.POST.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
    ):
        return redirect(next_url)
    return redirect("contactos:contacto_detail", pk=contacto.pk)
