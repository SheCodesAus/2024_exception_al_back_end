from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser, Skill, Interest


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    skills = SkillSerializer(many=True, read_only=True)
    interests = InterestSerializer(many=True, read_only=True)
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
            password = validated_data['password']
        )
        user.biography = validated_data.get('biography', '')
        user.profile_image = validated_data.get('profile_image', '')
        user.save()
        return user