from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

    def create(self,validated_data):
        password = validated_data['password']
        password_hash = make_password(password)
        user = User()

        user.name = validated_data.get('name')
        user.lastname = validated_data.get('lastname')
        user.email = validated_data.get('email')
        user.role = validated_data.get('role')

        user.password = password_hash
        user.save()
        return user
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        
        return {
            'id': instance['id'],
            'name': instance['name'],
            'lastname':instance['lastname'],
            'email': instance['email']
        }