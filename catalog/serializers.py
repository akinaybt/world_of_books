from rest_framework import serializers
from .models import Author, Book, BookInstance, Genre, Language, Status
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = '__all__'

    def get_author_name(self, obj):
        return obj.last_name, obj.first_name


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class BookSerializer(serializers.ModelSerializer):
    genre_title = serializers.SerializerMethodField()
    language_name = serializers.SerializerMethodField()

    def get_language_name(self, obj):
        return obj.language.name

    def get_genre_title(self, obj):
        return obj.genre.name

    class Meta:
        model = Book
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class BookInstanceSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = BookInstance
        fields = '__all__'

    def get_status(self, obj):
        return obj.status.name



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
