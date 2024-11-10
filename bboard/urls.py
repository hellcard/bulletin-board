from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:cat_id>/', views.cats, name = 'cats'),
    path('add/', views.BbCreateView.as_view(), name = 'add')
]