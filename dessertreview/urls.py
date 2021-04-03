from django.urls import path
from dessertreview import views

app_name = 'dessertreview'

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path("register/", views.register, name='register'),
    path("login/", views.user_login, name = 'login'),
    path("login/myaccount", views.my_account, name='my account'),
    path("login/myaccount/myreviews", views.my_reviews, name='my reviews'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('categories/', views.categories, name='categories'),
    path('shops/', views.shops, name='shops'),
    path('shop/<slug:shop_slug>/', views.show_shop, name='show_shop'),
    path('dessert/<slug:dessert_slug>/', views.show_dessert, name='show_dessert'),
    path('writeareview/<slug:writeareview_slug>/', views.show_review, name='show review'),
    path('writeareview/', views.write_a_review, name='write_a_review'),
    path('add_dessert/', views.add_dessert, name='add_dessert'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('add_category/', views.add_category, name='add_category'),
]
