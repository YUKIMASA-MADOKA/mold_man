from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Item
import datetime

import numpy as np
import pandas as pd

# Create your views here.
# --
# pandasを利用しsample.xlsから金型マスタ（Item）にデータをコピーする
# --

def index(request):
# アップロードなどに改善したほうがいいと思うが、
# 横着してフォルダにあるexcelを直接読み込み   
    df = pd.read_excel('sample.xls',sheet_name = 0 )

# 初期化（全削除）
    Item.objects.all().delete()
    ix = 0
    for row in df.values :
        ix = ix + 1

# 見出し行は読み飛ばし
        if ix < 3:
            continue
#        if ix > 10:
#            break

        obj = Item(
            department = row[0], # 管理籍
            is_drawing = yes_no(row[1]), # 製品図面
            is_not_our_molds = yes_no(row[2]), # 他社金型
            frame_code = row[3], # フレーム
            mold_code = row[4], # 中型
            manufacture_date = is_date(row[5]), # 製造年月
            name = is_char(row[6]), # 製品名
            molding_machine = row[7], # 成型機
            frame_height_moving_side = is_int(row[8]), # フレーム高さ 移動側
            frame_height_fix_side = is_int(row[9]), # フレーム高さ 固定側
            number_of = is_int(row[10]), # 取数
            weight = is_int(row[11]), # 目付
#            fm=is_int(row[12]), # 発泡倍率
#            fn=is_float(row[13]),   # 容積 0mm
#            fo=is_float(row[14]),   # 容積 1mm
#            fp=is_float(row[15]),   # 容積 3mm
            outer_length=is_int(row[16]), # 外寸 長さ
            outer_width=is_int(row[17]), # 外寸 幅
            outer_height=is_int(row[18]), # 外寸 高さ
            inner_length=is_int(row[19]), # 内寸 長さ
            inner_width=is_int(row[20]), # 内寸 幅
            inner_height=is_int(row[21]), # 内寸 深さ
#            fw=row[22], # 内底R
#            fx=row[23], # 立上りR
#            fy=is_int(row[24]), # 足
#            fz=is_float(row[25]),   # 肉厚 底
#            faa=is_float(row[26]), # 肉厚 長手側
#            fab=is_float(row[27]), # 肉厚 手持側
#            fac=yes_no(row[28]),   # 足 形状 ﾍﾞﾀ足
#            fad=yes_no(row[29]),   # 足 形状 ﾘﾝｸﾞ足
#            fae=yes_no(row[30]),   # 足 形状 その他
            is_lid=yes_no(row[31]),   # 蓋
            is_with_lid=yes_no(row[32]),   # 蓋付
#            fah=yes_no(row[33]),   # 銘板
#            fai=yes_no(row[34]),   # 銘板位置 長手側
#            faj=yes_no(row[35]),   # 銘板位置 手持側
#            fak=yes_no(row[36]),   # 勘合部 形状 Zﾀｲﾌﾟ
#            fal=yes_no(row[37]),   # 勘合部 形状 Nﾀｲﾌﾟ
#            fam=yes_no(row[38]),   # 勘合部 形状 Hﾀｲﾌ
#            fan=yes_no(row[39]),   # 勘合部 形状 落込
#            fao=yes_no(row[40]),   # 水抜
#            fap=yes_no(row[41]),   # 水抜き穴 形状 底丸穴
#            faq=yes_no(row[42]),   # 水抜き穴 形状 横穴
#            far=yes_no(row[43]),   # 水抜き穴 形状 ｺｰﾅｰ穴
#            fas=yes_no(row[44]),   # 水抜き穴 形状 水封式
#            fat=yes_no(row[45]),   # 水抜き穴 形状 縦穴式
#            fau=yes_no(row[46]),   # 水抜き穴 形状 排水式
#            fav=yes_no(row[47]),   # 仕切
#            faw=yes_no(row[48]),   # 特殊形状
            usage_notes=is_char(row[49]),   # 用途
#            fay=row[50],   # 小数点有
            memo = row[51],   # 備考
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

def is_char(s):
    if isinstance(s, str):
        return s
    else:
        return None

def yes_no(s):
    if s == 'Yes':
        return(True)
    else:
        return(False)

def is_date(s):
#    try:
#        x =  datetime.datetime.strptime(s, '%Y-%m-%d')
#    except ValueError:
#        return None
#    else:
#        return s
    if isinstance(s, datetime.datetime):
        return s
    else:
        return None


