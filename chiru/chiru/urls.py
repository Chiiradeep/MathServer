from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.power_calculator, name='power_calculator'),
]