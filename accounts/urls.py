from django.urls import path

from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
