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

    # 外寸（長さ、幅、高さ） 
    # gt ltが付かないFilterは検索には未使用（ラベル名を参照するために定義）
    # 以上・以下にするためgt ⇒ gte、lt ⇒ lteに変更（template側はgt ltのまま）
    #outer_length_xx = filters.NumericRangeFilter(field_name='outer_length', lookup_expr='100,300')
    outer_length = filters.NumberFilter()
    outer_length_gt = filters.NumberFilter(field_name='outer_length', lookup_expr='gte')
    outer_length_lt = filters.NumberFilter(field_name='outer_length', lookup_expr='lte')
    outer_width = filters.NumberFilter()
    outer_width_gt = filters.NumberFilter(field_name='outer_width', lookup_expr='gte')
    outer_width_lt = filters.NumberFilter(field_name='outer_width', lookup_expr='lte')
    outer_height = filters.NumberFilter()
    outer_height_gt = filters.NumberFilter(field_name='outer_height', lookup_expr='gte')
    outer_height_lt = filters.NumberFilter(field_name='outer_height', lookup_expr='lte')

    # 内寸（長さ、幅、高さ） 
    inner_length = filters.NumberFilter()
    inner_length_gt = filters.NumberFilter(field_name='inner_length', lookup_expr='gte')
    inner_length_lt = filters.NumberFilter(field_name='inner_length', lookup_expr='lte')
    inner_width = filters.NumberFilter()
    inner_width_gt = filters.NumberFilter(field_name='inner_width', lookup_expr='gte')
    inner_width_lt = filters.NumberFilter(field_name='inner_width', lookup_expr='lte')
    inner_height = filters.NumberFilter()
    inner_height_gt = filters.NumberFilter(field_name='inner_height', lookup_expr='gte')
    inner_height_lt = filters.NumberFilter(field_name='inner_height', lookup_expr='lte')

#    order_by = MyOrderingFilter(
#
#        fields=(
#            ('name', 'name'),
#        ),
#       field_labels={
#            'name': '製品名',
#        },
#        label='並び順'
#    )

    class Meta:
        model = Item
#        fields = ('department', 'name', 'sex', 'memo',)
#        fields = ('department', 'name', )
# 上で指定していればここで指定しなくても表示されるようになるみたい
        fields = ('department', 'name', 'outer_length_gt', 'outer_length_lt',)
#        fields = ('name', 'outer_length_gt', 'outer_length_lt',)
