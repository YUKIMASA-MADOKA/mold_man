# 2023.04.14 製造年月日をカレンダーコントロールで使えるように追加
import bootstrap_datepicker_plus.widgets as datetimepicker
#from bootstrap_datepicker_plus import datetimepicker

from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
#        fields = ('department','name','frame_code','molds_code','molding_machine','frame_height_moving_side','number_of','weight','age','sex','memo','is_drawing',)
#        fields = ('department','is_drawing','is_not_our_molds','name','frame_code','mold_code','created_at','molding_machine','frame_height_moving_side','number_of','weight','memo',)
        fields = (
                    'department',   # 管理籍
                    'is_drawing',   # 製品図面
                    'is_not_our_molds', # 他社金型
                    'frame_code',    # フレーム
                    'mold_code',    # 中型
                    'manufacture_date', # 製造年月
                    'name', # 製品名
                    'molding_machine',  # 成型機
                    'frame_height_moving_side', # フレーム高さ移動側
                    'frame_height_fix_side', # フレーム高さ固定側
                    'number_of',    # 取数
                    'weight',   # 目付

                    'outer_length',   # 外寸長さ
                    'outer_width',   # 外寸幅
                    'outer_height',   # 外寸高さ
                    'inner_length',   # 内寸長さ
                    'inner_width',   # 内寸幅
                    'inner_height',   # 内寸深さ

                    'is_lid', # 蓋
                    'is_with_lid', # 蓋付
                    'usage_notes', # 用途
                    'memo', # 備考
                )
        widgets = {
# デフォルトの表示をカスタマイズする場合に追記（必ずしも書かなくても良い　書かない場合はシステムの初期値）
#                    'department': forms.TextInput(attrs={'placeholder':'記入例：焼津'}),
                    'department': forms.Select(),
                    'is_drawing': forms.CheckboxInput(),
                    'is_not_our_molds': forms.CheckboxInput(),
                    'name': forms.TextInput(attrs={'placeholder':'記入例：HB-14A','onkeyup':'this.value = this.value.toUpperCase();'}),
                    'frame_code': forms.TextInput(attrs={'onkeyup':'this.value = this.value.toUpperCase();'}),
                    'mold_code': forms.TextInput(attrs={'style':'text-transform: uppercase;','pattern':'^[0-9A-Za-z]+$;'}),
#                    'created_at': forms.DateInput(),
#                    'created_at': datetimepicker.DatePickerInput(
                    'manufacture_date': datetimepicker.DatePickerInput(
#                        format='%Y-%m-%d',
# formatパラメータは将来無視されるようなのでoptionに書き換え
                        options={
                            'format': 'Y-M-D',
                            'locale': 'ja',
                            'dayViewHeaderFormat': 'YYYY年 MMMM',
                        }
                    ),
#                    'age': forms.NumberInput(attrs={'min':1}),
#                    'sex': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }

#
# -- 以降は、書き方の個人的なメモ等なので、後から消します。
# attrs={'onkeyup':'this.value = this.value.toUpperCase();'}
# attrs={'style':'text-transform: uppercase;'}
# attrs={'pattern':'^[0-9A-Za-z]+$;'}
	
#                    'code_a': forms.TextInput(attrs={'pattern':'^[A-Za-z0-9_@-]+$'}),
#                    'code_b': forms.URLInput(attrs={'style':'ime-mode: inactive;','inputmode':'url'}),
#                    'code_b': forms.TextInput(attrs={'onInput':'checkForm(this)'}),
