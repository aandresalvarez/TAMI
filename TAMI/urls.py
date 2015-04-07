from django.conf.urls import patterns, include, url
from django.contrib import admin
from nucleo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TAMI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^nucleo/', include('nucleo.urls')),
    url(r'^admin/', include(admin.site.urls)),
	# url(r'^marcador/', 'nucleo.views.Marcador', name='marcador'),
	#url(r'^$', views.index, name='index'),

	
)
