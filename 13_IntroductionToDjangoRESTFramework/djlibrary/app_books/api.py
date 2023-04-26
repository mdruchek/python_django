from rest_framework import viewsets
from django.db.models.query import QuerySet
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .pagination import MyCursorPagination


class AuthorViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения, создания, удаления и редактирования авторов"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = MyCursorPagination

    def get_queryset(self) -> QuerySet[Author]:
        """
        Метод, реализующий фильтрацию авторов по фамилии
        :return: список авторов
        :rtype: QuerySet
        """

        author_name = self.request.query_params.get('lastname')
        if author_name:
            self.queryset = self.queryset.filter(lastname=author_name)
        return self.queryset


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet для отображения, создания, удаления и редактирования книг"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyCursorPagination

    def get_queryset(self) -> QuerySet[Author]:
        """
        Метод, реализующий фильтрацию книг по фамилии автора, названию и количеству страниц
        :return: список авторов
        :rtype: QuerySet
        """
        author_name = self.request.query_params.get('author_lastname')
        if author_name:
            self.queryset = self.queryset.filter(author__lastname=author_name)

        book_name = self.request.query_params.get('book_name')
        if book_name:
            self.queryset = self.queryset.filter(name__icontains=book_name)
        print(self.request.query_params)

        number_pages = self.request.query_params.get('number_pages')
        if number_pages:
            self.queryset = self.queryset.filter(number_pages=number_pages)

        number_pages__lte = self.request.query_params.get('number_pages__lte')
        if number_pages__lte:
            self.queryset = self.queryset.filter(number_pages__lte=number_pages__lte)

        number_pages__gte = self.request.query_params.get('number_pages__gte')
        if number_pages__gte:
            self.queryset = self.queryset.filter(number_pages__gte=number_pages__gte)
        return self.queryset
