from django.db import models
from django.conf import settings

from django.core import validators
# Create your models here.

class Item(models.Model):

#    department = models.CharField(verbose_name='管理籍',max_length=255,choices=DEPARTMENT_CHOICES,default='焼津',)
    department = models.CharField('管理籍',max_length=255,choices=settings.DEPARTMENT_CHOICES,default=settings.MY_DEPARTMENT,)
    is_drawing = models.BooleanField('製品図面',default=True,)
    is_not_our_molds = models.BooleanField('他社金型',default=True,)
    frame_code = models.CharField('フレーム',validators=[validators.RegexValidator(regex=r'^[a-zA-Z0-9_@\-\.]+$')],max_length=255)
    mold_code = models.CharField('中型',max_length=255)
    manufacture_date = models.DateField('製造年月',blank=True, null=True)
    name = models.CharField('製品名', max_length=255, blank=True, null=True,)
    molding_machine = models.CharField('成型機',max_length=255, blank=True, null=True)
    frame_height_moving_side = models.IntegerField('フレーム高さ移動側',blank=True, null=True)
    frame_height_fix_side = models.IntegerField('フレーム高さ固定側',blank=True, null=True)
    number_of  = models.DecimalField('取数',max_digits=8, decimal_places=1, blank=True, null=True)
    weight = models.DecimalField('目付',max_digits=8, decimal_places=1, blank=True, null=True)
#    fm = models.IntegerField('M', blank=True, null=True)    # 発泡倍率
#    fn = models.DecimalField('N', max_digits=8, decimal_places=1, blank=True, null=True)    # 容積 0mm
#    fo = models.DecimalField('O', max_digits=8, decimal_places=1, blank=True, null=True)    # 容積 1mm
#    fp = models.DecimalField('P', max_digits=8, decimal_places=1, blank=True, null=True)    # 容積 3mm
    outer_length = models.IntegerField('外寸 長さ', blank=True, null=True)    # 外寸 長さ
    outer_width = models.IntegerField('外寸 幅', blank=True, null=True)    # 外寸 幅
    outer_height = models.IntegerField('外寸 高さ', blank=True, null=True)    # 外寸 高さ
    inner_length = models.IntegerField('内寸 長さ', blank=True, null=True)    # 内寸 長さ
    inner_width = models.IntegerField('内寸 幅', blank=True, null=True)    # 内寸 幅
    inner_height = models.IntegerField('内寸 深さ', blank=True, null=True)    # 内寸 深さ
 #   fw = models.CharField('W',max_length=255, blank=True, null=True)    # 内底R
 #   fx = models.CharField('X',max_length=255, blank=True, null=True)    # 立上りR
 #   fy = models.IntegerField('Y', blank=True, null=True)    # 足
 #   fz = models.DecimalField('Z', max_digits=8, decimal_places=1, blank=True, null=True)    # 肉厚 底
 #   faa = models.DecimalField('AA', max_digits=8, decimal_places=1, blank=True, null=True)  # 肉厚 長手側
 #   fab = models.DecimalField('AB', max_digits=8, decimal_places=1, blank=True, null=True)  # 肉厚 手持側
 #   fac = models.BooleanField('AC',default=True,)  # 足 形状 ﾍﾞﾀ足
 #   fad = models.BooleanField('AD',default=True,)  # 足 形状 ﾘﾝｸﾞ足
 #   fae = models.BooleanField('AE',default=True,)  # 足 形状 その他
    is_lid = models.BooleanField('蓋',default=True,)  # 蓋
    is_with_lid = models.BooleanField('蓋付',default=True,)  # 蓋付
 #   fah = models.BooleanField('AH',default=True,)  # 銘板
 #   fai = models.BooleanField('AI',default=True,)  # 銘板位置 長手側
 #   faj = models.BooleanField('AJ',default=True,)  # 銘板位置 手持側
 #   fak = models.BooleanField('AK',default=True,)  # 勘合部 形状 Zﾀｲﾌﾟ
 #   fal = models.BooleanField('AL',default=True,)  # 勘合部 形状 Nﾀｲﾌﾟ
 #   fam = models.BooleanField('AM',default=True,)  # 勘合部 形状 Hﾀｲﾌﾟ
 #   fan = models.BooleanField('AN',default=True,)  # 勘合部 形状 落込
 #   fao = models.BooleanField('AO',default=True,)  # 水抜
 #   fap = models.BooleanField('AP',default=True,)  # 水抜き穴 形状 底丸穴
 #   faq = models.BooleanField('AQ',default=True,)  # 水抜き穴 形状 横穴
 #   far = models.BooleanField('AR',default=True,)  # 水抜き穴 形状 ｺｰﾅｰ穴
 #   fas = models.BooleanField('AS',default=True,)  # 水抜き穴 形状 水封式
 #   fat = models.BooleanField('AT',default=True,)  # 水抜き穴 形状 縦穴式
 #   fau = models.BooleanField('AU',default=True,)  # 水抜き穴 形状 排水式
 #   fav = models.BooleanField('AV',default=True,)  # 仕切
 #   faw = models.BooleanField('AW',default=True,)  # 特殊形状
    usage_notes = models.CharField('用途',max_length=255, blank=True, null=True)  # 用途
 #   fay = models.CharField('AY',max_length=255, blank=True, null=True)  # 小数点有
 #   faz = models.CharField('AZ',max_length=255, blank=True, null=True)  # 備考
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
#        verbose_name='登録日',
#        verbose_name='製造日',
#        auto_now_add=True
        blank=True,
        null=True,
    )


#        validators=[validators.RegexValidator(regex=r'^[a-zA-Z0-9_@\-\.]+$')],

class Temp(models.Model):
    fa = models.CharField('A',max_length=255, blank=True, null=True)    # 管理籍
    fb = models.CharField('B',max_length=255, blank=True, null=True)    # 製品図面
    fc = models.CharField('C',max_length=255, blank=True, null=True)    # 他社金型
    fd = models.CharField('D',max_length=255, blank=True, null=True)    # フレーム
    fe = models.CharField('E',max_length=255, blank=True, null=True)    # 中型
    ff = models.CharField('F',max_length=255, blank=True, null=True)    # 製造年月
    fg = models.CharField('G',max_length=255, blank=True, null=True)    # 製品名
    fh = models.CharField('H',max_length=255, blank=True, null=True)    # 成型機
    fi = models.CharField('I',max_length=255, blank=True, null=True)    # フレーム高さ 移動側
    fj = models.CharField('J',max_length=255, blank=True, null=True)    # フレーム高さ 固定側
    fk = models.CharField('K',max_length=255, blank=True, null=True)    # 取数
    fl = models.CharField('L',max_length=255, blank=True, null=True)    # 目付
    fm = models.CharField('M',max_length=255, blank=True, null=True)    # 発泡倍率
    fn = models.CharField('N',max_length=255, blank=True, null=True)    # 容積 0mm
    fo = models.CharField('O',max_length=255, blank=True, null=True)    # 容積 1mm
    fp = models.CharField('P',max_length=255, blank=True, null=True)    # 容積 3mm
    fq = models.CharField('Q',max_length=255, blank=True, null=True)    # 外寸 長さ
    fr = models.CharField('R',max_length=255, blank=True, null=True)    # 外寸 幅
    fs = models.CharField('S',max_length=255, blank=True, null=True)    # 外寸 高さ
    ft = models.CharField('T',max_length=255, blank=True, null=True)    # 内寸 長さ
    fu = models.CharField('U',max_length=255, blank=True, null=True)    # 内寸 幅
    fv = models.CharField('V',max_length=255, blank=True, null=True)    # 内寸 深さ
    fw = models.CharField('W',max_length=255, blank=True, null=True)    # 内底R
    fx = models.CharField('X',max_length=255, blank=True, null=True)    # 立上りR
    fy = models.CharField('Y',max_length=255, blank=True, null=True)    # 足
    fz = models.CharField('Z',max_length=255, blank=True, null=True)    # 肉厚 底
    faa = models.CharField('AA',max_length=255, blank=True, null=True)  # 肉厚 長手側
    fab = models.CharField('AB',max_length=255, blank=True, null=True)  # 肉厚 手持側
    fac = models.CharField('AC',max_length=255, blank=True, null=True)  # 足 形状 ﾍﾞﾀ足
    fad = models.CharField('AD',max_length=255, blank=True, null=True)  # 足 形状 ﾘﾝｸﾞ足
    fae = models.CharField('AE',max_length=255, blank=True, null=True)  # 足 形状 その他
    faf = models.CharField('AF',max_length=255, blank=True, null=True)  # 蓋
    fag = models.CharField('AG',max_length=255, blank=True, null=True)  # 蓋付
    fah = models.CharField('AH',max_length=255, blank=True, null=True)  # 銘板
    fai = models.CharField('AI',max_length=255, blank=True, null=True)  # 銘板位置 長手側
    faj = models.CharField('AJ',max_length=255, blank=True, null=True)  # 銘板位置 手持側
    fak = models.CharField('AK',max_length=255, blank=True, null=True)  # 勘合部 形状 Zﾀｲﾌﾟ
    fal = models.CharField('AL',max_length=255, blank=True, null=True)  # 勘合部 形状 Nﾀｲﾌﾟ
    fam = models.CharField('AM',max_length=255, blank=True, null=True)  # 勘合部 形状 Hﾀｲﾌﾟ
    fan = models.CharField('AN',max_length=255, blank=True, null=True)  # 勘合部 形状 落込
    fao = models.CharField('AO',max_length=255, blank=True, null=True)  # 水抜
    fap = models.CharField('AP',max_length=255, blank=True, null=True)  # 水抜き穴 形状 底丸穴
    faq = models.CharField('AQ',max_length=255, blank=True, null=True)  # 水抜き穴 形状 横穴
    far = models.CharField('AR',max_length=255, blank=True, null=True)  # 水抜き穴 形状 ｺｰﾅｰ穴
    fas = models.CharField('AS',max_length=255, blank=True, null=True)  # 水抜き穴 形状 水封式
    fat = models.CharField('AT',max_length=255, blank=True, null=True)  # 水抜き穴 形状 縦穴式
    fau = models.CharField('AU',max_length=255, blank=True, null=True)  # 水抜き穴 形状 排水式
    fav = models.CharField('AV',max_length=255, blank=True, null=True)  # 仕切
    faw = models.CharField('AW',max_length=255, blank=True, null=True)  # 特殊形状
    fax = models.CharField('AX',max_length=255, blank=True, null=True)  # 用途
    fay = models.CharField('AY',max_length=255, blank=True, null=True)  # 小数点有
    faz = models.CharField('AZ',max_length=255, blank=True, null=True)  # 備考

    # 管理サイト上の表示設定
#    def __str__(self):
#        return self.name
        
#    class Meta:
#        verbose_name = 'アイテム'
#        verbose_name_plural = 'アイテム'
