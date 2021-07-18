
from django.contrib import admin
from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('todoapp/', include('todoapp.urls')),
]
