from django.urls import path
from . import views

app_name = 'inicio'

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('modo_incognito/', views.modo_incognito, name='modo_incognito'),
]