from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('export/', views.export_tasks, name='export_tasks'),
    path('import/', views.import_tasks, name='import_tasks'),
]
