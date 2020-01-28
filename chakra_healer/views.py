from rest_framework import generics
from .serializers import ChakrasSerializer, UserDataSerializer, ConditionsSerializer
from .models import Chakras, Conditions, UserData
from rest_framework import permissions

class ChakrasList(generics.ListCreateAPIView):
    queryset = Chakras.objects.all()
    serializer_class = ChakrasSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ConditionsList(generics.ListCreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ConditionsDetail(generics.ListCreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserList(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = (permissions.IsAuthenticated,)