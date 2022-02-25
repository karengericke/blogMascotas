from django import forms

   
class fMascotas(forms.Form):
    nombre=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    edad=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))
    raza=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    trucos=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
class fDuenios(forms.Form):
    nombre=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    apellido=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    edad=forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'}))

class fRopita(forms.Form):
    nombre = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    marca = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    color = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z,á,Á,é,É,í,Í,ó,Ó,ú,Ú,ñ,Ñ, ,]+', 'title':'Solo se permiten letras'}))
    precio = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[0-9 ]+', 'title':'Solo se permiten números'})) 