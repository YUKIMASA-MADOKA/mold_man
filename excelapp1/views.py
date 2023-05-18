from django.shortcuts import render
import os
import openpyxl
import pprint
from django.http import HttpResponse
from django.conf import settings
from app.models import Item
from datetime import date

def index(request):
    """
      Excel output from template
    """
    # Excelのテンプレートファイルの読み込み
    # wb = openpyxl.load_workbook('C:/data/python/exceltemplates/sample.xlsx')
    # （ひな形Excel配備場所が絶対PATHだとデプロイ時に困りそうなので相対PATH指定に）
    wb = openpyxl.load_workbook(os.path.join(settings.BASE_DIR, 'excelapp1/sample.xlsx').replace(os.sep,'/'))

    # 検索条件は（'query'という名称の）セッションに保存されるのでそれを参照
    query = request.session.get('query')

    sheet = wb['sheet1']
# 見出しはexcelテンプレート側で定義
#    sheet['A2'] = '管理籍'
#    sheet['G3'] = '製品名'
    sheet['C2'] = query['department'] # 管理籍
    sheet['C3'] = query['outer_length_gt']  # 外寸長さ（From）
    sheet['C4'] = query['outer_width_gt']  # 外寸幅（From）
    sheet['C5'] = query['outer_height_gt']  # 外寸高さ（From）
    sheet['E3'] = query['outer_length_lt']  # 外寸長さ（To）
    sheet['E4'] = query['outer_width_lt']  # 外寸幅（To）
    sheet['E5'] = query['outer_height_lt']  # 外寸高さ（To）
    sheet['H3'] = query['inner_length_gt']  # 内寸長さ（From）
    sheet['H4'] = query['inner_width_gt']  # 内寸幅（From）
    sheet['H5'] = query['inner_height_gt']  # 内寸高さ（From）
    sheet['J3'] = query['inner_length_lt']  # 内寸長さ（To）
    sheet['J4'] = query['inner_width_lt']  # 内寸幅（To）
    sheet['J5'] = query['inner_height_lt']  # 内寸高さ（To）
    sheet['M3'] = query['name'] # 製品名

# 見出しはexcelテンプレート側で定義
#    sheet['A10'] = '管理籍'
#    sheet['B10'] = '製品名'
#    sheet['C10'] = '中型'
#    sheet['D10'] = '外寸長'
#    sheet['E10'] = '外寸幅'
#    sheet['F10'] = '外寸高'
#    sheet['G10'] = '内寸長'
#    sheet['H10'] = '内寸幅'
#    sheet['I10'] = '内寸深'
#    sheet['J10'] = '蓋'
#    sheet['K10'] = '蓋付'
#    sheet['L10'] = '製造年月'
#    sheet['M10'] = '用途'
    
    # contains（部分一致）にすると管理籍もいい感じに抽出されるのでとりあえずif文なしで
    items = Item.objects.filter(department__contains=query['department'],name__contains=query['name'])
#    items = Item.objects.all()
    
    i = 10
    for item in items :
        i = i + 1
        sheet['A'+str(i)] = item.department # 管理籍
        sheet['B'+str(i)] = item.name   # 製品名
        sheet['C'+str(i)] = item.mold_code  # 中型
        sheet['D'+str(i)] = item.outer_length  # 外寸長さ
        sheet['E'+str(i)] = item.outer_width  # 外寸幅
        sheet['F'+str(i)] = item.outer_height  # 外寸高さ
        sheet['G'+str(i)] = item.inner_length  # 内寸長さ
        sheet['H'+str(i)] = item.inner_width  # 内寸幅
        sheet['I'+str(i)] = item.inner_height  # 内寸深さ
        sheet['J'+str(i)] = item.is_lid  # 蓋
        sheet['K'+str(i)] = item.is_with_lid  # 蓋つき
#        dt = datetime.date.item.manufacture_date
#        sheet['L'+str(i)] = dt.strfdate("%Y/%m") # 製造年月
        sheet['L'+str(i)] = item.manufacture_date # 製造年月
        sheet['M'+str(i)] = item.usage_notes  # 用途

# Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response
