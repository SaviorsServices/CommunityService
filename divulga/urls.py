from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^formevent/$', views.formevent, name='formevent'),
    url(r'^mapa', views.mapa, name='mapa'),
    url(r'^servicolist', views.servicolist, name='servicolist'),


]