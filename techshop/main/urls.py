from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup_user,name='signup'),
]
