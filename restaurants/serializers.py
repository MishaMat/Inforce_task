from rest_framework import serializers
from .models import *


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantModel
        fields = '__all__'


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_staff']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = MenuModel
        fields = '__all__'


