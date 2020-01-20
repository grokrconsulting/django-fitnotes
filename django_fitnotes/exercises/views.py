from django_filters import rest_framework as filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from exercises.filters import SetFilter
from exercises.models import Category, Exercise, Set
from exercises.pagination import LimitOffset100Pagination
from exercises.serializers import CategorySerializer, ExerciseSerializer, SetSerializer


class CategoryReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffset100Pagination


class ExerciseReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    pagination_class = LimitOffset100Pagination


class SetReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    pagination_class = LimitOffset100Pagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SetFilter
