from django_filters.rest_framework import FilterSet

from api.models import Computer


class ComputerFilterSet(FilterSet):
    from django_filters import filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Computer
        fields = ["brand", "min_price", "max_price"]
