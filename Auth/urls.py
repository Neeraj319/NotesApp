from django.contrib import admin
from django.urls import path, include
from .views import login_user, sigin_user, logout_user
urlpatterns = [
    path('login/', login_user, name='login'),
    path('SignUp', sigin_user, name='signin'),
    path('logout', logout_user, name='logout')
]
