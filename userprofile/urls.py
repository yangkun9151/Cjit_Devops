from django.urls import path
from . import views


app_name = 'userprofile'
urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('loginout/', views.login_out, name="loginout"),
]