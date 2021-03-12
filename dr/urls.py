from django.urls import path
from dr import views

app_name = 'dr'

urlpatterns = [
    path('', views.home, name='home'),
]
