from django.conf.urls import url

from .views import keyboard
from .views import message

urlpatterns = [
    url(r'^keyboard/', keyboard),
    url(r'^message/', message),
]
