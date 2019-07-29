from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='TOOD名', lookup_expr='contains')
    memo = filters.CharFilter(label='内容', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': 'TODO名',
            'age': '日付',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'sex', 'memo',)
