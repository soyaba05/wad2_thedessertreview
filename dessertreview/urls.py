from django.urls import path
from dessertreview import views

app_name = 'dessertreview'

urlpatterns = [
    path('', views.home, name='home'),
]
