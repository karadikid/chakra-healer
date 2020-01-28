from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('chakras/', views.ChakrasList.as_view(), name='chakras_list'),
    path('conditions/', views.ConditionsList.as_view(), name='condition_list'),
    path('conditions/<int:pk>', views.ConditionsDetail.as_view(), name='condition_detail'),
    path('users/', views.UserList.as_view(), name='chakras_list'),
    path('users/<int:pk>', views.UserDetails.as_view(), name='chakras_list'),
]

