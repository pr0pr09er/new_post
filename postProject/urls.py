from django.contrib import admin
from django.urls import path
from postApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add_new),
    path('', views.all_posts),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]

