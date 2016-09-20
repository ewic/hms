from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("This is the index view")

def form(request):
	return HttpResponse("This is the form view")

def list(request):
	return HttpResponse("This is the list view")

