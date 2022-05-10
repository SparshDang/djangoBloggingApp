from django.urls import path
from authApp import views

app_name = 'auth'
urlpatterns = [
    path('signin/', views.AccountCreateView.as_view(), name='signIn'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('<int:pk>', views.AccountView.as_view(), name='account'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
]
