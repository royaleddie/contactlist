from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcontact/', views.addContact, name='addcontact'),
    path('profile/<str:pk>', views.contactProfile, name='profile'),
    path('editcontact/<str:pk>', views.editContact, name='editcontact'),
]