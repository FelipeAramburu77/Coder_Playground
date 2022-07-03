from random import choices
from django import forms

class Local_Formulario(forms.Form):
    name=forms.CharField(max_length=50, label="Fantasy name")
    CITY = (
        (0, "Select"),
        (1, "Córdoba"),
        (2, "Capital Federal"),
        (3, "Rosario"),
        (4, "Mendoza"),
        (5, "Salta"))
    city= forms.ChoiceField(choices=CITY, required=True, label="In which city the mall is?",initial=0)
    address= forms.CharField(max_length=50, label="Enter the address")
    mall_number= forms.IntegerField(min_value=0)
    DAYS=(
        (0, "Select"),
        (1, "Monday to friday"),
        (2, "Monday to saturday"),
        (3, "Monday to monday"),
    )    
    opening_hours=forms.ChoiceField(choices=DAYS,required=True, label="Which days does the mall open?",initial=0)

class Vendedor_Formulario(forms.Form):
    name= forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    email= forms.EmailField()
    mall_number= forms.CharField()
    birthday= forms.DateField()

class Producto_Formulario(forms.Form):
    product= forms.CharField(max_length=30, label="Product name")
    prize= forms.FloatField(min_value=0, label="Enter prize, please")
    marcas=(
        (0, 'Select'),
        (1, 'Apple'),
        (2, 'Samsung'),
        (3, 'Huawei'),
        (4, 'Sony')
    )   
    brand= forms.ChoiceField(choices=marcas,required=True, label='Enter brand, please')
    stock= forms.IntegerField(min_value=0, label="Available stock")