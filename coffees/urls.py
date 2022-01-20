from django.urls import path

from .import views
app_name = 'coffees'
urlpatterns = [
    # ex: /coffees/
    path('', views.index ,name='index'),
    path('<int:pk>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.show, name='show'),
    path('add/', views.add, name='add'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]