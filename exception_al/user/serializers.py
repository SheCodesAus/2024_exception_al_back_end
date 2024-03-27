from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'biography', 'profile_image', 'skills', 'interests', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'], 
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            email = validated_data['email'],
            password = validated_data['password'],
        )
        user.biography = validated_data.get('biography', '')
        user.profile_image = validated_data.get('profile_image', '')
        user.skills = validated_data.get('skills', '')
        user.interests = validated_data.get('interests', '')
        user.save()
        return user

# code source modified from https://medium.com/django-rest/django-rest-framework-change-password-and-update-profile-1db0c144c0a3
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('password', 'new_password', 'new_password2')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"password": "Password fields do not match."})

        return attrs

    def validate_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"password": "Existing password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance