from django import forms
from AppPagina.models import sex, tit

YEARS= [x for x in range(1910,2021)]

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    comision = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=YEARS))       
    sexo = forms.ChoiceField(choices=sex)
    
class MaestroFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=YEARS))       
    sexo = forms.ChoiceField(choices=sex)
    titulo = forms.ChoiceField(choices=tit)
    
    