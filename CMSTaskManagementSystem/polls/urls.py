from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('board/<int:board_id>/', views.board, name='board'),
    path('add_board/', views.add_board, name='add_board'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_board/<int:board_id>/', views.delete_board, name='delete_board'),
    path('update-task-state/', views.update_task_state, name='update_task_state'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('get_task/<int:task_id>/', views.get_task, name='get_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('first_board/', views.first_board, name='first_board'),  
    path('add_user/<int:board_id>/', views.add_user, name='add_user'),
    path('add_user_next/', views.add_user_next, name='add_user_next'),
    path('board_selector/', views.board_selector, name='board_selector'),
    path('leave_board/<int:board_id>/', views.leave_board, name='leave_board'),
]