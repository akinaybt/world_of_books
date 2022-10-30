from django.contrib import admin
from .models import (
    Author, Book, Genre, Language, Status, BookInstance
)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', 'date_of_birth', 'date_of_death']


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', Book.display_author)
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status', 'due_back')

    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')
                             }),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')
                                             }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
