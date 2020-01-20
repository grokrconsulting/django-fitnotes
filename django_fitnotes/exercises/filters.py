from django_filters import rest_framework as filters


from exercises.models import Set


class SetFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Set
        fields = ["exercise", "date"]
