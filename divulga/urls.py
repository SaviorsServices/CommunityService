from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^formevent/$', views.formevent, name='formevent'),
]