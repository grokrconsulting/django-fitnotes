from rest_framework.pagination import LimitOffsetPagination


class LimitOffset100Pagination(LimitOffsetPagination):
    default_limit = 100
