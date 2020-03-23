from django.contrib import admin
from django.urls import path

from hello.views import hello, sync_hello

urlpatterns = [
    path('', hello, name='hello'),
    path('sync/', sync_hello, name='sync_hello'),
    path('admin/', admin.site.urls),
]
