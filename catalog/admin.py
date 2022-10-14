from django.contrib import admin
from .models import (
    Author, Book, Genre, Language, Status, BookInstance
)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', Book.display_author)
    list_filter = ('genre', 'author')


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
