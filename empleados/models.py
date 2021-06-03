from django.db import models
from django.contrib.auth.models import User

from utils.models import UserProfile, UserProfileBaseModel 
# Create your models here.


class Empleado(UserProfileBaseModel): 
    user = models.OneToOneField(User, related_name="Empleado",blank = True, null = True, on_delete =models.CASCADE)
    apellido_paterno= models.CharField(max_length=255, blank=True, null=True) 
    apellido_materno= models.CharField(max_length=255, blank=True, null=True) 
    home_district= models.CharField(max_length=255, blank=True, null=True) 
    fecha_entrada= models.DateField( blank=True, null=True)
    #entry_designation= models.CharField(max_length=255, blank=True, null=True) 
    # entry_scale = models.CharField(max_length=255, blank=True, null=True) 
    # picture = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)     
    # archive_status = models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
    status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 
    def get_full_name(self):
        return self.user.first_name+" "+self.user.last_name
        
    def __str__(self):
        return self.user.username

class Accion_Disciplinaria(models.Model):
	empleado = models.ForeignKey(Empleado, blank=True, null=True,related_name='Accion_Disciplinaria',on_delete=models.CASCADE)
	comentario = models.CharField(max_length=255, blank=True, null=True) 
	sancion = models.CharField(max_length=255, blank=True, null=True) 
	fecha = models.DateField( blank=True, null=True)

class Educacion(models.Model):  
	empeado = models.ForeignKey(Empleado, blank=True, null=True,related_name='Educacion',on_delete=models.CASCADE)
	nombre_institucion= models.CharField(max_length=255, blank=True, null=True) 
	grado = models.CharField(max_length=255, blank=True, null=True) 
	anho = models.CharField(max_length=255, blank=True, null=True) 
	#division = models.CharField(max_length=255, blank=True, null=True) 

class Capacitacion(models.Model): 
    empleado = models.ForeignKey(Empleado, blank = True, null = True, related_name='Capacitacion', on_delete = models.CASCADE)
    titulo_capacitacion = models.CharField(max_length = 255, blank = True, null = True)
    institucion = models.CharField(max_length=255, blank = True, null = True)
    fecha_inicio = models.DateField(blank = True, null = True)
    fecha_termino = models.DateField(blank = True , null = True)
    tipo_capacitacion = models.CharField(max_length = 255, blank = True, null = True)

class Ascenso(models.Model): 
    empleado = models.ForeignKey(Empleado, blank = True, null = True, related_name='Ascenso', on_delete = models.CASCADE)
    fecha_ascenso = models.DateField(blank = True, null = True)
    puesto  = models.CharField(max_length = 255, blank = True, null = True)
    escala_pago = models.CharField(max_length=255, blank = True, null = True)

class Dias_libres(models.Model): 
    empleado = models.ForeignKey(Empleado, blank = True, null = True, related_name='Dias_libres', on_delete = models.CASCADE)
    fecha_inicio = models.DateField(blank = True, null = True)
    fecha_termino = models.DateField(blank = True , null = True)

class Retiro(models.Model):
    empleado = models.ForeignKey(Empleado, blank = True, null = True, related_name='Retiro', on_delete = models.CASCADE)
    anho = models.DateField(blank = True, null = True)
    fecha = models.DateField(blank = True, null = True)

class Historial_Servicio(models.Model):
    empleado = models.ForeignKey(Empleado, blank = True, null = True, related_name='Historial_Servicio', on_delete = models.CASCADE)
    puesto  = models.CharField(max_length = 255, blank = True, null = True)
    area = models.CharField(max_length = 255, blank = True, null = True)
    seccion =  models.CharField(max_length = 255, blank = True, null = True)
    fecha_inicio = models.DateField(blank = True, null = True)
    fecha_termino = models.DateField(blank = True, null = True)

