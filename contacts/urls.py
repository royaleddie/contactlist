from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcontact/', views.addContact, name='addcontact')
]