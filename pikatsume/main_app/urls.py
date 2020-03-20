from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pikabase/', views.pikabase_index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pikabase/new/', views.new_pika, name='new_pika'),
    path('profile/', views.update_profile, name='profile'),
    path('accounts/signup', views.signup, name='signup')
]