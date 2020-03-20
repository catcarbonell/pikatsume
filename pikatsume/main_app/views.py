from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Pika, Ptype
from .forms import PikaForm
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pikabase')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = { 'form' : form, 'error_message' : error_message }
    return render(request, 'registration/signup.html', context)

def home(request):
    return HttpResponse('<h1>Pika! (o^.^o)</h1>')

def about(request):
    return  render(request, 'about.html')

def pikabase_index(request):
    pikas = Pika.objects.all()
    return  render(request, 'pikabase/index.html', { 'pikas': pikas })

@login_required
def new_pika(request):
    if request.method == 'POST':
        new_form = PikaForm(request.POST)
        if new_form.is_valid():
            pika = new_form.save(commit="False")
            pika.user = request.user
            pika.save()
            return redirect ('pikabase/index.html', pika.id)
    else:
        new_form = PikaForm()
        context = {  'new_form' : new_form  }
        return render(request, 'pikabase/pika_form.html', context)