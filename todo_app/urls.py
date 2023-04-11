from django.contrib import admin
from django.urls import path
from todo_app import views

app_name = 'todo_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('todos/', views.current_todos, name='current_todos'),
    path('completed/', views.completed_todos, name='completed_todos'),
    path('todos/<int:pk>', views.view_todo, name='view_todo'),
    path('todos/<int:pk>/complete', views.complete_todo, name='complete_todo'),
    path('todos/<int:pk>/repeat', views.repeat_todo, name='repeat_todo'),
    path('todos/<int:pk>/delete', views.delete_todo, name='delete_todo'),
    path('create/', views.create_todo, name='create_todo')
]
