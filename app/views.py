#from django.shortcuts import render
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item

# item_filter.htmlに配置したラジオの値を取得したい
#from django.shortcuts import render
#from django import forms

# Create your views here.
# 検索一覧画面
#class ItemFilterView(LoginRequiredMixin, FilterView):
class ItemFilterView(FilterView):
    model = Item

    # デフォルトの並び順を新しい順とする　⇒　管理籍、製品名順にする　⇒　検討中
    # queryset = Item.objects.all().order_by('-created_at')
    # queryset = Item.objects.all().order_by('department', 'name' )
    # 表示量が多いと動作が重くなるので先頭300件のみの表示に制限
    queryset = Item.objects.all()[:300]

    # 初期値を設定したい2023.04.12 ⇒　検索の初期値は無くても良さそう（検索条件はセッションにキャッシュされるので、そのほうが便利かも）
    #ItemFilter['initial'] = {'department':'沼津'}

    # django-filter用設定
    filterset_class = ItemFilter
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

# 詳細画面
#class ItemDetailView(LoginRequiredMixin, DetailView):
class ItemDetailView(DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')
