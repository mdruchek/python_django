from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    ordering = 'id'