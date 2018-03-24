
from django.urls import path, include
from blogapp import views

urlpatterns = [
    path('', views.Allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]
