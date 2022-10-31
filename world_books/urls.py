from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('language', views.LanguageViewSet)
router.register('genres', views.GenreViewSet)
router.register('status', views.StatusViewSet)
router.register('book_instance', views.BookInstanceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('client/auth/', views.RegisterAPI.as_view(), name='registration'),
]
