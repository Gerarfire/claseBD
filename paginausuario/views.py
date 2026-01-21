from django.shortcuts import render
from django.http import HttpResponse

def pagina_bienvenida(request):
	return HttpResponse("<h1>HOJA DE VIDA<h1>")
# Create your views here.
