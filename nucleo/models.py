from django.db import models
from datetime import datetime
import precarga
from django.contrib.auth.models import User
# Create your models here.
class Marcador(models.Model):
		nombre = models.CharField(max_length=200,unique=True)
		##percentil 99
		percentil_superior = models.DecimalField(max_digits=10,decimal_places=2,default=0)
		## percentil 1
		percentil_inferior = models.DecimalField(max_digits=10,decimal_places=2,default=0)
		
		def __str__(self):
			return self.nombre
		# def __str__(self):
			# return self.percentil_superior
		# def __str__(self):
			# return self.percentil_inferior
		# def	 load_default_percentiles (self):
			# for i in precarga.Marc_per:
				# A=Marcador(nombre=i["variable"],percentil_superior=i["sup"],percentil_inferior=i["inf"])
				# A.save()
		# def delete_everything(self):
			# Reporter.objects.all().delete()

class Enfermedad(models.Model):
		nombre = models.CharField(max_length=200,unique=True)
		sigla= models.CharField(max_length=200)
		Descripcion = models.TextField()
		marcadores_por_enfermedad = models.ManyToManyField(Marcador)
		def __str__(self):
			return "Nombre: "+ self.nombre + " - Sigla: "+ self.sigla
		# def __str__(self):
			# return self.Descripcion
			
class Madre(models.Model):
		nombre = models.CharField(max_length=200,unique=True)
		apellido = models.CharField(max_length=200,unique=True)
		dob = models.DateTimeField('date of birth')
		email= models.EmailField(max_length=70,blank=True)
		Observaciones = models.TextField()
		def __str__(self):
			return self.nombre
		
		# def dob_recent(self):
			# return self.dob >= timezone.now() - datetime.timedelta(days=1)
			
class Lote(models.Model):
	 	user = models.ForeignKey(User)#Foranea a los usuarios 
		dou = models.DateTimeField(blank=True)##fecha de carga del lote
		# xls_path = models.FilePathField(path="/home/images", match="foo.*", recursive=True)
		def __str__(self):
			 return "Usuario: "+str(self.user)+"- Fecha:"+str(self.dou)
			
				
class Neonato(models.Model):
		madre = models.ForeignKey(Madre)
		lote = models.ForeignKey(Lote)
		enfermedad_por_neonato = models.ManyToManyField(Enfermedad)
		marcadores_por_neonato = models.ManyToManyField(Marcador,through='Valor_marcadores_de_cada_neonato')
		codigo = models.CharField(max_length=200,unique=True)
		nombre = models.CharField(max_length=200)
		apellido = models.CharField(max_length=200)
		dob = models.DateTimeField('date of birth')
		result_path = models.CharField(max_length=200)
		#marcador = models.ManyToManyField(Marcador)
		def __str__(self):
			return  "Codigo: " + str(self.codigo) +" - Nombre: "+str(self.nombre)+" "+str(self.apellido)
		
		
class Valor_marcadores_de_cada_neonato(models.Model):
		# id = models.AutoField(primary_key=True,default=0)
		marcador = models.ForeignKey(Marcador)
		neonato = models.ForeignKey(Neonato)
		valor = models.DecimalField(max_digits=15,decimal_places=2,default=0)
		unique_together = ("marcador", "neonato")
		def __str__(self):
			return str(self.valor)
		# def __str__(self):
			# return self.neonato	

###PRegarga de datos de la aplicacion	
	
			