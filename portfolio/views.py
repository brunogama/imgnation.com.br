# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from annoying.decorators import render_to

from models import Trabalho

@render_to('template.html')
def trabalhos(request, slug):
	trabalhos = Trabalho.objects.all()
	trabalho = get_object_or_404(Trabalho, slug=slug)
	return { "trabalho" : trabalho }
	
	

@render_to('pages/games.html')
def games(request):
	games = Trabalho.objects.filter(category__category_title="Games")
	return { "games" : games }
	
@render_to('pages/apps.html')
def apps(request):
	apps = Trabalho.objects.filter(category__category_title="Apps")
	return { "apps" : apps }