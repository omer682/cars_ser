from rest_framework import serializers
from .models import Person, Car, Rent, ContactUs
from django.contrib.auth import get_user_model


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
    
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'age']

class CarSerializer(serializers.ModelSerializer):
    owner_personal_id = serializers.SerializerMethodField()
    owner_age = serializers.SerializerMethodField()
    def get_owner_personal_id(self, car):
        return car.owner.person_id if car.owner else None

    def get_owner_age(self, car):
        return car.owner.age if car.owner else None
    class Meta:
        model = Car
        fields = '__all__'