from knox.models import AuthToken
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Author, Book, BookInstance, Genre, Language, Status
from .serializers import (
    BookSerializer, RegisterSerializer,
    UserSerializer, AuthorSerializer,
    LanguageSerializer, StatusSerializer,
    GenreSerializer, BookInstanceSerializer
)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def registration_view(request, format=None):
    content = {'user': str(request.user),  # `django.contrib.auth.User` instance.
               'auth': str(request.auth),  # None
               }
    return Response(content)


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BookInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()
