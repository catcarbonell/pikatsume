from django.shortcuts import render
from django.http import HttpResponse
from .models import Pika
# Create your views here.

def home(request):
    return HttpResponse('<h1>Pika! (o^.^o)</h1>')

def about(request):
    return  render(request, 'about.html')

def pikabase_index(request):
    pikas = Pika.objects.all()
    return  render(request, 'pikabase/index.html', { 'pikas': pikas })