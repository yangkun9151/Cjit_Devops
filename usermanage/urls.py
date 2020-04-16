from django.urls import path
from . import views

app_name = 'usermanage'
urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
]