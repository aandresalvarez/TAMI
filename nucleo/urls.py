from django.conf.urls import patterns, url

from nucleo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	# url(r'^marcador/$',views.marcador,name='marcador'),
	url(r'^marcador/', views.Marcadores, name='marcador'),
	url(r'^enfermedades/', views.Enfermedades, name='enfermedad'),
	url(r'^neonatos/', views.Neonatos, name='neonato'),
)