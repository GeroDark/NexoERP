from django.urls import path

from . import views


app_name = "contactos"

urlpatterns = [
    path("", views.contacto_list, name="contacto_list"),
    path("nuevo/", views.contacto_create, name="contacto_create"),
    path(
        "nuevo/empresa/<int:empresa_id>/",
        views.contacto_create_for_empresa,
        name="contacto_create_for_empresa",
    ),
    path("<int:pk>/", views.contacto_detail, name="contacto_detail"),
    path("<int:pk>/editar/", views.contacto_update, name="contacto_update"),
    path("<int:pk>/desactivar/", views.contacto_deactivate, name="contacto_deactivate"),
]
