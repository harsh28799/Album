from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album,Song

def index(request):
	all_albums=Album.objects.all()
	context={
		'all_albums': all_albums,
	}
	return render(request,'home/index.html',context)

def detail(request, album_id):
	try:
		album=Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request,'home/detail.html',{'album':album})
