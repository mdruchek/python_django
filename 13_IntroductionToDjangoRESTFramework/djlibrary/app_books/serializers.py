from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели Author"""

    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'year_birth']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели Book"""

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'isbn', 'year_release', 'number_pages']
