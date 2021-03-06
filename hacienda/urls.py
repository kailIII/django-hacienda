from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('^login/', include('login.urls')),
    url('^reporte/', include('reportes.urls')),
    url('^contrib/', include('contribuyentes.urls')),
    url(r'^liquidacion', include('liquidaciones.urls')),
    url(r'^sdr/$', 'contribuyentes.views.lista_contribuyentes'),
    url(r'^$', 'login.views.home', name='home'),
)
