from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.home_page, name='home'),
    path('create_task',views.create_task, name='create_task'),
    path('create_category',views.create_category,name='create_category'),
    path('',views.category_list,name='category_list'),
    path('delete_category/<int:category_id>/', views.delete_category,name='delete_category'),
    path('category_tasks/<int:category_id>',views.category_tasks,name='category_tasks'),
]