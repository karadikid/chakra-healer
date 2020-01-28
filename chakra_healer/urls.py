from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('chakras/', views.ChakrasList.as_view(), name='chakras_list'),
    path('conditions/', views.ConditionsList.as_view(), name='condition_list'),
    path('users/', views.UserList.as_view(), name='users_list'),
]

