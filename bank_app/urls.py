from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('details/', views.details, name='details'),
    path('get-branches/', views.get_branches, name='get_branches'),
    path('add/', views.add, name='add'),

]
