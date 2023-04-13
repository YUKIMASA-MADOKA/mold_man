from django_filters import FilterSet
from django_filters import filters

from django.conf import settings
from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

#    department = filters.CharFilter(label='管理籍', lookup_expr='contains')
    department = filters.ChoiceFilter(label='管理籍',choices=settings.DEPARTMENT_CHOICES,)
    name = filters.CharFilter(label='製品名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
#            ('age', 'age'),
            ('created_at', 'create_at'),
        ),
        field_labels={
            'name': '製品名',
#            'age': '年齢',
            'created_at': '製造年月日',
        },
        label='並び順'
    )

    class Meta:
        model = Item
#        fields = ('department', 'name', 'sex', 'memo',)
        fields = ('department', 'name', 'memo',)
