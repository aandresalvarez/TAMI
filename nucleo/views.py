from django.shortcuts import render_to_response, get_object_or_404
from nucleo.models import Marcador,Enfermedad ,Neonato
from django.template import RequestContext
# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def Cargar_Lotes(request):
	# marcadores= Marcador.objects.all()
	# return render_to_response('marcadores.html',{'marcadores':marcadores})

# def Marcadores(request):
    # marcadores1= Marcador.objects.all()
    # paginator = Paginator(marcadores1, 10) # Show 25 contacts per page

    # page = request.GET.get('page')
    # try:
        # marcadores = paginator.page(page)
    # except PageNotAnInteger:
        # # If page is not an integer, deliver first page.
        # marcadores = paginator.page(2)
    # except EmptyPage:
        # # If page is out of range (e.g. 9999), deliver last page of results.
        # marcadores = paginator.page(paginator.num_pages)

    # return render_to_response('marcadores.html',{'marcadores':marcadores})	
	
def Marcadores(request):
	 marcadores= Marcador.objects.all()
	 return render_to_response('marcadores.html',{'marcadores':marcadores})
	 
def Enfermedades(request):
	enfermedades=Enfermedad.objects.all()
	return render_to_response('enfermedades.html',{'enfermedades':enfermedades})
	
def Neonatos(request):
	neonatos=Neonato.objects.all()
	return render_to_response('neonatos.html',{'neonatos':neonatos})	 
	 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")