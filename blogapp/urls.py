from django.urls import path

from blogapp import views

app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('allPosts/', views.AllPostsView.as_view(), name='allPosts'),
    path('postDetail/<int:pk>', views.PostDetailView.as_view(), name='postDetail'),
    path('postCreate/', views.PostCreateView.as_view(), name='postCreate'),
]
