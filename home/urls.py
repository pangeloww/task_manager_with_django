from django.urls import path
from .views import custom_404
from home import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]

handler404 = 'home.views.custom_404'
