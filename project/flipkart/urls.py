from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from flipkart.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing,name='landing')
]


