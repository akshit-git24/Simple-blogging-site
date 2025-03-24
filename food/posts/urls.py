from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('',views.posts_lists, name="list"),
    path('home/',views.Homepage,name="Home"),
    path('new-post/',views.new_post,name="new-post"),
    path('<slug:slug>',views.post_page, name="page"),
] 