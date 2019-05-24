from django.conf.urls import url
from . import views

urlpatterns = [
	
	#/home/
    url(r'^$', views.index, name='index'),
    
    #/home/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]