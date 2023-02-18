from django.urls import path
from portfolio import views

app_name = 'portfolio'


urlpatterns = [
    path('<pk>', views.view_project, name='view_project'),
]
