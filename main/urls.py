from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('todo/', views.todo, name='todo'),
    path('todo/edit/<int:pk>/', views.todo_edit, name='todo_edit'),
    path('todo/delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('todo/mark_done/<int:pk>/', views.todo_mark_done, name='todo_mark_done'),
] 