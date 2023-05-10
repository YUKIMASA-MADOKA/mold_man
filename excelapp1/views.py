from django.shortcuts import render
import os
import openpyxl
import pprint
from django.http import HttpResponse
from django.conf import settings
from app.models import Item

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
    sheet['A1'] = '管理籍'
    sheet['A2'] = '製品名'
    sheet['B1'] = query['department']
    sheet['B2'] = query['name']

    sheet['A10'] = '管理籍'
    sheet['B10'] = '製品名'
    sheet['C10'] = '中型'
    
    # contains（部分一致）にすると管理籍もいい感じに抽出されるのでとりあえずif文なしで
    items = Item.objects.filter(department__contains=query['department'],name__contains=query['name'])
#    items = Item.objects.all()
    
    i = 10
    for item in items :
        i = i + 1
        sheet['A'+str(i)] = item.department
        sheet['B'+str(i)] = item.name
        sheet['C'+str(i)] = item.mold_code

# Excelを返すためにcontent_typeに「application/vnd.ms-excel」をセットします。

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'report.xlsx'

    # データの書き込みを行なったExcelファイルを保存する
    wb.save(response)

    # 生成したHttpResponseをreturnする
    return response
