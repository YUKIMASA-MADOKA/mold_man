from django.db import models
from django.core import validators
# Create your models here.

class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )
    IS_DRAWING_CHOICES = (
        (1, 'はい'),
    )
    IS_NOT_OUR_MOLDS = (
        (1, 'はい'),
    )
    name = models.CharField(
#        verbose_name='名前',
#        max_length=200,
        verbose_name='製品名',
        max_length=255,
    )
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
#        verbose_name='登録日',
        verbose_name='製造日',
        auto_now_add=True
    )
    department = models.CharField(verbose_name='管理籍',max_length=255)
    is_drawing = models.BooleanField(verbose_name='製品図面',default=True,)
    is_not_our_molds = models.BooleanField(verbose_name='他社金型',default=True,)
    frame_code = models.CharField(verbose_name='フレーム',max_length=255)
    molds_code = models.CharField(verbose_name='中型',max_length=255)
#    manufacture_date = models.DateField(blank=True, null=True)
#    name = models.CharField(max_length=255)
    molding_machine = models.CharField(verbose_name='成型機',max_length=255, blank=True, null=True)
    frame_height_moving_side = models.IntegerField(verbose_name='フレーム高さ移動側',blank=True, null=True)
    frame_height_fix_side = models.IntegerField(verbose_name='フレーム高さ固定側',blank=True, null=True)
    number_of  = models.DecimalField(verbose_name='取数',max_digits=8, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField(verbose_name='目付',max_digits=8, decimal_places=1, blank=True, null=True)

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'