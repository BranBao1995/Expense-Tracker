from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('main/', views.main, name='main'),
    path('edit/<str:target>/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('signup/', views.signup_user, name='signup')
    # manual login
    # path('login/', views.auth_login, name='login')
]