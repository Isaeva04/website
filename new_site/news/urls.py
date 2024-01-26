from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    #path('news/', views.news),
    path('', views.news_index, name="news_index"),
    path('<int:pk>/', views.news_detail, name="news_detail"),

]
