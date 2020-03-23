from django.contrib import admin
from django.urls import path

from hello.views import hello

urlpatterns = [
    path('', hello, name='hello'),
    path('admin/', admin.site.urls),
]
