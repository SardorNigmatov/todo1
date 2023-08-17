from django.urls import path
from .views import AllTask, DetailTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('get_all/',AllTask.as_view(),name='get_all'),
    path('get_by_id/<int:pk>/',DetailTask.as_view(),name='get_by_id'),
    path('created/',CreateTask.as_view(),name='created'),
    path('update/<int:pk>/',UpdateTask.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteTask.as_view(),name='delete')
]