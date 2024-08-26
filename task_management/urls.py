from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.home_page, name='home'),
    path('create_task',views.create_task, name='create_task'),
    path('create_category',views.create_category,name='create_category'),
]