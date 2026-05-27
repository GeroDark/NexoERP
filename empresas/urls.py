from django.urls import path

from . import views


app_name = "empresas"

urlpatterns = [
    path("", views.empresa_list, name="empresa_list"),
    path("nueva/", views.empresa_create, name="empresa_create"),
    path("<int:pk>/", views.empresa_detail, name="empresa_detail"),
    path("<int:pk>/editar/", views.empresa_update, name="empresa_update"),
    path("<int:pk>/desactivar/", views.empresa_deactivate, name="empresa_deactivate"),
]
