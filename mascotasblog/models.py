from django.db import models

# Create your models here.
  
class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    raza = models.CharField(max_length=30)
    trucos = models.CharField(max_length=30,null=True)
    
    def __str__(self):
        if(self.trucos == None):
            response = f"{self.nombre} - {self.edad} años, de raza {self.raza}"
        else:
            response = f"{self.nombre} - {self.edad} años, de raza {self.raza} y sabe {self.trucos}"          
        return response
           
class Duenio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
      
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad} años"
    
class Ropita(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    precio = models.IntegerField() 
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} de color {self.color} con un precio de ${self.precio} USD"
    
