from django.conf.urls import url

from .views import keyboard

urlpatterns = [
       url(r'^keyboard/', keyboard)
    ]
