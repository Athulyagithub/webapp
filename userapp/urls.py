from . import views
from django.urls import path
# app_name='user'
urlpatterns = [



    path('', views.detail, name='home'),
    path('view/<int:movie_id>/',views.view,name='view'),
    path('user_movies/', views.user_movies, name='user_movies'),

    path('index', views.index, name='index'),
    path('update/<int:id>/', views.update, name='update'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('search_by_category/', views.search_by_category, name='search_by_category'),

    path('movie/', views.movie, name='movie'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.add, name='add'),
    path('review/', views.review, name='review'),
    path('category/', views.category, name='category'),
    path('delete/<int:id>/', views.delete, name='delete'),

]

