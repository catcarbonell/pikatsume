from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pikabase/', views.pikabase_index, name='index'),
    path('pikabase/new/', views.new_pika, name='new_pika'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup')
]