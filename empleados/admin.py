from django.contrib import admin



## modelos de la app
from empleados.models import Empleado
from empleados.models import Educacion, Capacitacion, Accion_Disciplinaria
from empleados.models import Ascenso, Dias_libres, Retiro, Historial_Servicio 

# Register your models here.

class Accion_DisciplinariaInLine(admin.TabularInline): 
    model = Accion_Disciplinaria
    extra = 1

class EducacionInLine(admin.TabularInline):
   model = Educacion
   extra  = 1

class CapacitacionInLine(admin.TabularInline): 
    model = Capacitacion
    extra = 1 

class AscensoInLine(admin.TabularInline): 
    model = Ascenso
    extra = 1

class Dias_libresInLine(admin.TabularInline): 
    model = Dias_libres
    extra = 1

class Historial_ServicioInLine(admin.TabularInline):
    model = Historial_Servicio
    extra = 1

class RetiroInLine(admin.TabularInline): 
    model = Retiro
    extra = 1

class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    inlines = [Accion_DisciplinariaInLine, EducacionInLine,
             CapacitacionInLine, AscensoInLine, Dias_libresInLine,
             Historial_ServicioInLine, RetiroInLine]


admin.site.register(Empleado, EmpleadoAdmin)
