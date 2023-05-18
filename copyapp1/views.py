from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Item ,Temp

# Create your views here.
# --
# 一時テーブル（）に取込みしたデータを金型マスタ（Item）にコピーする
# --

def index(request):
    temps = Temp.objects.all()[:500]   # テスト用に先頭500件
#    temps = Temp.objects.all()
    # 初期化（全削除）
    Item.objects.all().delete()
    for temp in temps :
        obj = Item(
            department = temp.fa, # 管理籍
            is_drawing = yes_no(temp.fb), # 製品図面
            is_not_our_molds = yes_no(temp.fc), # 他社金型
            frame_code = temp.fd, # フレーム
            mold_code = temp.fe, # 中型
            manufacture_date = temp.ff, # 製造年月
            name = temp.fg, # 製品名
            molding_machine = temp.fh, # 成型機
            frame_height_moving_side = is_int(temp.fi), # フレーム高さ 移動側
            frame_height_fix_side = is_int(temp.fj), # フレーム高さ 固定側
            number_of = is_int(temp.fk), # 取数
            weight = is_int(temp.fl), # 目付
#            fm=is_int(temp.fm), # 発泡倍率
#            fn=is_float(temp.fn),   # 容積 0mm
#            fo=is_float(temp.fo),   # 容積 1mm
#            fp=is_float(temp.fp),   # 容積 3mm
            outer_length=is_int(temp.fq), # 外寸 長さ
            outer_width=is_int(temp.fr), # 外寸 幅
            outer_height=is_int(temp.fs), # 外寸 高さ
            inner_length=is_int(temp.ft), # 内寸 長さ
            inner_width=is_int(temp.fu), # 内寸 幅
            inner_height=is_int(temp.fv), # 内寸 深さ
#            fw=temp.fw, # 内底R
#            fx=temp.fx, # 立上りR
#            fy=is_int(temp.fy), # 足
#            fz=is_float(temp.fz),   # 肉厚 底
#            faa=is_float(temp.faa), # 肉厚 長手側
#            fab=is_float(temp.fab), # 肉厚 手持側
#            fac=yes_no(temp.fac),   # 足 形状 ﾍﾞﾀ足
#            fad=yes_no(temp.fad),   # 足 形状 ﾘﾝｸﾞ足
#            fae=yes_no(temp.fae),   # 足 形状 その他
            is_lid=yes_no(temp.faf),   # 蓋
            is_with_lid=yes_no(temp.fag),   # 蓋付
#            fah=yes_no(temp.fah),   # 銘板
#            fai=yes_no(temp.fai),   # 銘板位置 長手側
#            faj=yes_no(temp.faj),   # 銘板位置 手持側
#            fak=yes_no(temp.fak),   # 勘合部 形状 Zﾀｲﾌﾟ
#            fal=yes_no(temp.fal),   # 勘合部 形状 Nﾀｲﾌﾟ
#            fam=yes_no(temp.fam),   # 勘合部 形状 Hﾀｲﾌ
#            fan=yes_no(temp.fan),   # 勘合部 形状 落込
#            fao=yes_no(temp.fao),   # 水抜
#            fap=yes_no(temp.fap),   # 水抜き穴 形状 底丸穴
#            faq=yes_no(temp.faq),   # 水抜き穴 形状 横穴
#            far=yes_no(temp.far),   # 水抜き穴 形状 ｺｰﾅｰ穴
#            fas=yes_no(temp.fas),   # 水抜き穴 形状 水封式
#            fat=yes_no(temp.fat),   # 水抜き穴 形状 縦穴式
#            fau=yes_no(temp.fau),   # 水抜き穴 形状 排水式
#            fav=yes_no(temp.fav),   # 仕切
#            faw=yes_no(temp.faw),   # 特殊形状
            usage_notes=temp.fax,   # 用途
#            fay=temp.fay,   # 小数点有
            memo = temp.faz,   # 備考
            )
        obj.save()
    
    return HttpResponseRedirect('../?page=1')

def is_float(s):
    try:
        i = float(s)
    except ValueError:
        return None
    else:
        return i

def is_int(s):
    try:
        i = int(float(s))
    except ValueError:
        return None
    else:
        return i

def yes_no(s):
    if s == 'Yes':
        return(True)
    else:
        return(False)


# -- ここからは（メモ）データの全削除方法など　最終版は削除予定
# from app.models import Item, Mold
# Mold.objects.all().delete()