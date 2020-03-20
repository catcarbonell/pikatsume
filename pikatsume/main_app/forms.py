from django import forms
from .models import Pika

class PikaForm(forms.ModelForm):
    class Meta:
        model = Pika
        fields = ('name', 'pic_url')

