from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    """Класс разбивки на страницы"""

    ordering = 'id'