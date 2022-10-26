from django.urls import path
from .views import admin_approval, index, login_user, register

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('admin_approval/', admin_approval, name='admin_approval'),
]