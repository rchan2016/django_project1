from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('perform_two_numbers', views.perform_two_numbers, name='perform_two_numbers'),
    # path('add', views.add, name='add'),
]
