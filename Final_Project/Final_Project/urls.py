"""Final_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name='Inicio'),
    path('locales',views.locales, name='Locales'),
    path('locales_formulario', views.locales_formulario, name="Locales_Formulario"),    
    path('vendedores',views.vendedores, name='Vendedores'),
    path('vendedores_formulario',views.vendedores_formulario, name="Vendedores_Formulario"),    
    path('productos',views.productos, name='Productos'),
    path('productos_formulario',views.productos_formulario, name="Productos_Formulario"),
    path('buscar_local/',views.buscar_local, name="Buscar_Local"),
]
