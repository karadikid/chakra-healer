from rest_framework import serializers
from .models import Chakras,UserData,Conditions

class ChakrasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chakras
        fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = '__all__'

class ConditionsDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conditions
        fields = '__all__'
