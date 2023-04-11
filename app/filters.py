from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    department = filters.CharFilter(label='管理籍', lookup_expr='contains')
    name = filters.CharFilter(label='製品名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': '製品名',
            'age': '年齢',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('department', 'name', 'sex', 'memo',)
