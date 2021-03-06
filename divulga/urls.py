from django.conf.urls import url
from . import views


urlpatterns = [

    # url(r'^formevent/$', views.formevent, name='formevent'),
    url(r'^mapa/(?P<id>\d+)/$', views.mapa, name='mapa'),
    url(r'^servicolist/$', views.servicolist, name='servicolist'),
    url(r'^create_establishment', views.create_establishment, name='create_establishment'),
    url(r'^create_health_service', views.create_health_service, name='create_health_service'),
    url(r'^create_donation', views.create_donation, name='create_donation'),
    url(r'^create_voluntary', views.create_voluntary, name='create_voluntary'),

    # edit
    url(r'^edit_establishment/(?P<id>\d+)/$', views.edit_establishment, name='edit_establishment'),
    url(r'^edit_health_service/(?P<id>\d+)/$', views.edit_health_service, name='edit_health_service'),
    url(r'^edit_donation/(?P<id>\d+)/$', views.edit_donation, name='edit_donation'),
    url(r'^edit_voluntary/(?P<id>\d+)/$', views.edit_voluntary, name='edit_voluntary'),

    # delete
    url(r'^delete_establishment/(?P<id>\d+)/$', views.delete_establishment, name='delete_establishment'),
    url(r'^delete_health_service/(?P<id>\d+)/$', views.delete_health_service, name='delete_health_service'),
    url(r'^delete_donation/(?P<id>\d+)/$', views.delete_donation, name='delete_donation'),
    url(r'^delete_voluntary/(?P<id>\d+)/$', views.delete_voluntary, name='delete_voluntary'),

    # list
    url(r'^list_establishment/', views.list_establishment, name='list_establishment'),
    url(r'^list_health_service/', views.list_health_service, name='list_health_service'),
    url(r'^list_donation/', views.list_donation, name='list_donation'),
    url(r'^list_voluntary/', views.list_voluntary, name='list_voluntary'),

    url(r'^fale-conosco/(?P<id>\d+)/$', views.fale_conosco, name='fale-conosco'),
    url(r'^perfil/(?P<id>\d+)/$', views.perfil, name='perfil'),






]
