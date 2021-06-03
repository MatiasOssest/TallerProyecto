from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


from utils.country_codes import COUNTRY_CHOICES

# se crean los modelos bases para las aplicaciones
class BaseModel(models.Model):
     fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank = True)
     fecha_modif = models.DateTimeField(auto_now = True)
     creado_por  = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', null=True,blank=True, on_delete=models.CASCADE)
     modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modifiedby', null=True,blank=True, on_delete=models.CASCADE)
     
     class Meta:
         abstract = True

class AdressBaseModel(models.Model):
    direccion1 = models.CharField(max_length=255, blank = True, null = True)
    direccion2 = models.CharField(max_length=255, blank = True, null = True)
    pais = models.CharField(max_length=255, choices = COUNTRY_CHOICES, blank = True, null = True)
    ciudad = models.CharField(max_length=255, blank = True, null = True)
    codigo_postal = direccion1 = models.CharField(max_length=255, blank = True, null = True)

    class Meta: 
        abstract = True 


class UserProfile(models.Model): 
    user = models.OneToOneField(User, related_name='profile', on_delete = models.CASCADE, primary_key= True)
    nombre = models.CharField(max_length=255, blank = True, null = True)
    apellidos = models.CharField(max_length=255, blank = True, null = True)
    genero = models.CharField(max_length=32, choices=(('Masculino','Masculino'),('Femenino','Femenino'),('Otro','Otro'),('Prefieron no decir', 'No Info')), blank=True)
    fecha_nacimiento = models.DateField(blank = True, null =True)
    nacionalidad =  models.CharField(max_length=255, blank=True, null=True) 
    email = models.CharField(max_length=255, blank=True, null=True) 
    telefono = models.CharField(max_length=255, blank=True, null=True) 
    pais =  models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True) 
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    detalles_contacto =  models.TextField(blank=True, null=True)

    def get_full_name(self): 
        return self.user.nombre+' '+self.user.apellidos

    def __str__(self):
        return self.user.username 

User.perfil = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])

class UserProfileBaseModel(models.Model): 
    nombre            = models.CharField(max_length=255, blank=True, null=True) 
    apellidos         = models.CharField(max_length=255, blank=True, null=True) 
    genero            = models.CharField(max_length=32, choices=(('Masculino','Masculino'),('Femenino','Femenino'),('Otro','Otro'),('Prefieron no decir', 'No Info')), blank=True)   
    fecha_nacimiento  = models.DateField( blank=True, null=True)
    nacionalidad      = models.CharField(max_length=255, blank=True, null=True) 
    email             = models.CharField(max_length=255, blank=True, null=True) 
    telefono          = models.CharField(max_length=255, blank=True, null=True) 
    pais              = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    ciudad            = models.CharField(max_length=255, blank=True, null=True) 
    codigo_postal     = models.CharField(max_length=255, blank=True, null=True) 
    direccion         = models.TextField(blank=True, null=True)
    detalles_contacto = models.TextField(blank=True, null=True)
    
    class Meta:
       abstract = True