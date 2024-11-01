from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.log,name='login'),
    path('logout/',views.out,name='logout')
]
