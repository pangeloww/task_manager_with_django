from django.urls import path

from aboutus import views

urlpatterns = [
    path('', views.AboutUsView.as_view(), name='about us'),
    path('bulletin/', views.gather_emails_for_bulletins, name='gather')
]