from django import forms
from django.forms.fields import ImageField
from AppPagina.models import sex, tit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
    

class RegistroFormulario(UserCreationForm):
    username = forms.CharField()
    email= forms.EmailField()
    #pass1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #pass2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput) """
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    image_avatar = forms.IntegerField(required=False)
    
    
    #class Meta:
    #    model = User
    #    fields = ['username', 'email', 'last_name', 'first_name' ]
    #    help_text = {k:"" for k in fields}
    
   
    
    