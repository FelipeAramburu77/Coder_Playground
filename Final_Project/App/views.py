from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import *
from App.forms import *

# Create your views here.
def inicio(request):
      return render(request, "App/index.html")




def locales(request):
      locales = Locales.objects.all()
      return render(request, "App/locales.html", {"locales":locales})

def locales_formulario(request):
      if request.method == "POST":
            mi_formulario = Local_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  local = Locales (name=informacion['name'],city=informacion['city'],address=informacion['address'], mall_number=informacion['mall_number'],opening_hours=informacion['opening_hours'])
                  local.save()
                  return redirect("Locales") 
            else:
                  return render(request,"App/locales_formulario.html",{"mi_formulario":mi_formulario})
            
      else: 
            formulario_vacio = Local_Formulario()
            return render(request, "App/locales_formulario.html", {"mi_formulario":formulario_vacio})

def buscar_local(request):   
    if request.method == "POST":    
        mall_number = request.POST["mall_number"]    
        locales = Locales.objects.filter(mall_number__icontains=mall_number)
        return render(request,"App/buscar_local.html",{"locales":locales})
    
    else:
        locales = []     
        return render(request,"App/buscar_local.html",{"locales":locales})  




def vendedores(request):
      vendedores = Vendedores.objects.all()
      return render(request, "App/vendedores.html", {"vendedores":vendedores})

def vendedores_formulario(request):
      if request.method == "POST":
            mi_formulario = Vendedor_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  vendedor = Vendedores(name=informacion['name'], last_name=informacion['last_name'], email=informacion['email'], mall_number=informacion['mall_number'], birthday=informacion['birthday'])
                  vendedor.save()
                  return redirect("Vendedores") #Vuelvo al inicio o a donde quieran
            else:
                  return render(request, "App/vendedores_formulario.html", {"mi_formulario":mi_formulario})
      else: 
            formulario_vacio = Vendedor_Formulario()
            return render(request, "App/vendedores_formulario.html", {"mi_formulario":formulario_vacio})





def productos(request):
      productos = Productos.objects.all
      return render(request, "App/productos.html", {"productos":productos})
    
def productos_formulario(request):
      if request.method == "POST":
            mi_formulario = Producto_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  producto = Productos (product=informacion['product'], prize=informacion['prize'], brand=informacion['brand'], stock=informacion['stock'])
                  producto.save()
                  return redirect("Productos") #Vuelvo al inicio o a donde quieran
            else:
                  return render(request,"App/productos_formulario.html",{"mi_formulario":mi_formulario})
      else:
            formulario_vacio = Producto_Formulario()     
            return render(request, "App/productos_formulario.html", {"mi_formulario":formulario_vacio})

