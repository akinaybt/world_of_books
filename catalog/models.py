from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги", verbose_name="Жaнp книги")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилю автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения автора", verbose_name="Дата рождения", blank=True,
                                     null=True)
    date_of_death = models.DateField(help_text="Введите дату смерти автора", verbose_name="Дата смерти", blank=True,
                                     null=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text=" Выберите жанр для книги",
                              verbose_name="Жaнp книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text=" Выберите язык для книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги", verbose_name="Автор книги")
    summary = models.TextField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает URL-aдpec для доступа к определенному экземпляру книги.
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ','.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True)
    imprint = models.CharField(max_length=200)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
