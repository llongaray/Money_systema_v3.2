from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('rh.urls')),
    path('', include('ti.urls')),
    path('', include('financeiro.urls')),
]
