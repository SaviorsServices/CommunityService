from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^formevent/$', views.formevent, name='formevent'),
    url(r'^mapa/(?P<id>\d+)/$', views.mapa, name='mapa'),
    url(r'^servicolist/$', views.servicolist, name='servicolist'),
    url(r'^create_establishment', views.create_establishment, name='create_establishment'),
    url(r'^create_health_service', views.create_health_service, name='create_health_service'),
    url(r'^create_donation', views.create_donation, name='create_donation'),

]
