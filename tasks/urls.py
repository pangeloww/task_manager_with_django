from django.urls import path

from tasks import views

urlpatterns = [
    path('create/', views.create_task, name='create task'),
    path('edit/<int:pk>/', views.edit_task, name='edit task'),
    path('delete/<int:pk>/', views.delete_task, name='delete task'),
    path('details/<int:pk>/', views.task_details, name='task details'),
    path('alltasks/', views.all_tasks, name='all tasks'),
]
