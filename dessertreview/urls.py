from django.urls import path
from dessertreview import views

app_name = 'dessertreview'

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about_us, name='about us'),
    path('review/', views.review, name='review'),
    path('review/makeareview/', views.make_a_review, name='make a review'),
    path("register/", views.register, name='register'),
    path("login/", views.user_login, name='login'),
    path("login/myaccount", views.my_account, name='my account'),
    path("login/myaccount/myreviews", views.my_reviews, name='my reviews'),
    path('logout/', views.user_logout, name='logout'),
]