#from django.shortcuts import render
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
# from django.db.models import Q
from django.conf import settings

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item

# Create your views here.
# 検索一覧画面（ログイン無しでも使用可の仕様のため、LoginRequiredMixinは外してあります。画面制御はtemplateの「if user.is_authenticated」タグで制御）
#class ItemFilterView(LoginRequiredMixin, FilterView):
class ItemFilterView(FilterView):
    model = Item

    # デフォルトの並び順を新しい順とする　⇒　管理籍、製品名順にする　⇒　検討中
    # queryset = Item.objects.all().order_by('-created_at')
    # queryset = Item.objects.all().order_by('department', 'name' )[:100]

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

    #
    # 初期表示用（検索項目がひとつも指定されていないとき、先頭100件のみ表示）
    #
    def get_queryset(self):
        cnt = 0
        # 検索項目の一覧
        keys = ['department', 'name', 
         'outer_length_gt', 'outer_length_lt', 'outer_width_gt', 'outer_width_lt', 'outer_height_gt', 'outer_height_lt'
         'inner_length_gt', 'inner_length_lt', 'inner_width_gt', 'inner_width_lt', 'inner_height_gt', 'inner_height_lt']
        for key in keys:
            if (self.request.GET.get(key)):
                cnt = cnt + 1
        # 検索項目がひとつも指定されていない場合は先頭100件だけに（全件表示すると画面描画に時間がかかるため）、100では無く0でもよいかも
        if cnt == 0:
            self.queryset = Item.objects.all()[:100]

        return super().get_queryset()

    #
    # 検索結果の件数を画面表示、多すぎる場合は条件見直しをメッセージ
    # ※多すぎる場合はメッセージだけで制約は無し
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
#        count = self.queryset.count()
        count = self.filterset.qs.count()
        ctx['add_value'] = settings.MY_ADDVALUE

        # 検索結果が多い場合のメッセージおよび検索結果件数の表示を追加する
        if count > 500 :
            ctx['count_message'] = '：対象件数が多すぎます。検索条件を見直してください。'
        else:
            ctx['count_message'] = ''
        ctx['count'] = count

        # 検索条件に指定された項目を識別できるように見出しに色付け
        ctx['fil_department'] = 0
        ctx['fil_name'] = 0
        ctx['fil_outer_length'] = 0
        ctx['fil_outer_width'] = 0
        ctx['fil_outer_height'] = 0
        ctx['fil_inner_length'] = 0
        ctx['fil_inner_width'] = 0
        ctx['fil_inner_height'] = 0

        if (self.request.GET.get('department')):
            ctx['fil_department'] = 1
        if (self.request.GET.get('name')):
            ctx['fil_name'] = 1

        if (self.request.GET.get('outer_length_gt')):
            ctx['fil_outer_length'] = 1
        if (self.request.GET.get('outer_length_lt')):
            ctx['fil_outer_length'] = 1
        if (self.request.GET.get('outer_width_gt')):
            ctx['fil_outer_width'] = 1
        if (self.request.GET.get('outer_width_lt')):
            ctx['fil_outer_width'] = 1
        if (self.request.GET.get('outer_height_gt')):
            ctx['fil_outer_height'] = 1
        if (self.request.GET.get('outer_height_lt')):
            ctx['fil_outer_height'] = 1

        if (self.request.GET.get('inner_length_gt')):
            ctx['fil_inner_length'] = 1
        if (self.request.GET.get('inner_length_lt')):
            ctx['fil_inner_length'] = 1
        if (self.request.GET.get('inner_width_gt')):
            ctx['fil_inner_width'] = 1
        if (self.request.GET.get('inner_width_lt')):
            ctx['fil_inner_width'] = 1
        if (self.request.GET.get('inner_height_gt')):
            ctx['fil_inner_height'] = 1
        if (self.request.GET.get('inner_height_lt')):
            ctx['fil_inner_height'] = 1

        return ctx



# 詳細画面（ログイン無しでも使用可）
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
