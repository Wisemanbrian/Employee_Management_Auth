from django.urls import path
from .views import signup, login, reset_password, new_password

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('reset-password/', reset_password, name='reset_password'),
    path('new-password/<str:token>/', new_password, name='new_password'),
]
