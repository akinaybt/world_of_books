from knox.models import AuthToken
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Author, Book, BookInstance, Genre
from .serializers import BookCreateSerializer, BookUpdateSerializer, BookDeleteSerializer, RegisterSerializer, \
    UserSerializer, AuthorSerializer, LoanedBooksSerializer


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


class BookListView(ListCreateAPIView):
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()


class BookDestroyAPIView(DestroyAPIView):
    serializer_class = BookDeleteSerializer
    queryset = Book.objects.all()
    lookup_field = 'title'


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def registration_view(request, format=None):
    content = {'user': str(request.user),  # `django.contrib.auth.User` instance.
               'auth': str(request.auth),  # None
               }
    return Response(content)




