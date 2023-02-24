from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('main/', views.main, name='main'),
    path('edit/', views.edit, name='edit'),
]