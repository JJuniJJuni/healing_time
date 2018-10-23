from django.conf.urls import url
from django.contrib import admin

from inform.views import message
from inform.views import keyboard


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^keyboard/', keyboard),
    url(r'^message', message),
]
