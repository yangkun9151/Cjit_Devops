from django.urls import path
from . import views


app_name = 'server'
urlpatterns = [
    path('server-list/', views.server_list, name="server_list"),
    path('add-server/', views.add_server, name="add_server"),
    path('delete-server/', views.delete_server, name="delete_server"),
    path('edit-server/<int:id>/', views.edit_server, name="edit_server"),
]