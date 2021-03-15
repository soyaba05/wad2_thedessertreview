from django.conf.urls import path
from rango import views


app_name = 'dessertreview'

urlpatterns = [
    path("", views.index, name='index'),
    path("register/", views.register, name='register'),
    path("login/", views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]