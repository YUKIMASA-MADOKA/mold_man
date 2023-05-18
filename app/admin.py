from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Item ,Temp


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'name', 'mold_code')

    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'


class TempResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Temp


@admin.register(Temp)
class TempAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'fa','fb','fc','fd','fe','ff','fg','fh','fi','fj','fk','fl','fm','fn','fo','fp','fq','fr','fs','ft','fu','fv','fw','fx','fy','fz','faa','fab','fac','fad','fae','faf','fag','fah','fai','faj','fak','fal','fam','fan','fao','fap','faq','far','fas','fat','fau','fav','faw','fax','fay','faz')

    # django-import-exportsの設定
    resource_class = TempResource
