from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('book-create/', views.BookListView.as_view()),
    path('book-delete/<str:title>/', views.BookDestroyAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('client/auth/', views.RegisterAPI.as_view(), name='registration'),
]
