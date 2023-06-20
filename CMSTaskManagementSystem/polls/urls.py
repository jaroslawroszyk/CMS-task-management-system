from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('board/', views.board, name='board'),
    path('add_board/', views.add_board, name='add_board'),
]