from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
from .models import Veterinarian, AnimalPatient

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Veterinarian)
admin.site.register(AnimalPatient)
