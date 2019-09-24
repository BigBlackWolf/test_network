from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers

from . import services
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser', 'is_staff')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'body', 'total_likes', 'title')

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return services.is_fan(obj, user)


class FanSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
        )

    @staticmethod
    def get_username(obj):
        return obj.get_username()
