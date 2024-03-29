from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('profile/', views.profile, name="profile"),


    #CRUD VIEWS
    path('create_post/', views.createPost, name="create_post"),
    path('update_post/<slug:slug>', views.updatePost, name="update_post"),
]