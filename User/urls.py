from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('',views.Homepage,name="Home"),
    path('register/',views.registers, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('profile/', views.user_profile, name='user_profile'),
]
