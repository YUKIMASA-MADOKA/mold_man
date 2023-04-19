# 2023.04.14 製造年月日をカレンダーコントロールで使えるように追加
import bootstrap_datepicker_plus.widgets as datetimepicker
#from bootstrap_datepicker_plus import datetimepicker

from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
#        fields = ('department','name','frame_code','molds_code','molding_machine','frame_height_moving_side','number_of','weight','age','sex','memo','is_drawing',)
        fields = ('department','is_drawing','is_not_our_molds','name','frame_code','mold_code','created_at','molding_machine','frame_height_moving_side','number_of','weight','memo',)
        widgets = {
#                    'department': forms.TextInput(attrs={'placeholder':'記入例：焼津'}),
                    'department': forms.Select(),
                    'is_drawing': forms.CheckboxInput(),
                    'is_not_our_molds': forms.CheckboxInput(),
                    'name': forms.TextInput(attrs={'placeholder':'記入例：HB-14A','onkeyup':'this.value = this.value.toUpperCase();'}),
                    'frame_code': forms.TextInput(attrs={'onkeyup':'this.value = this.value.toUpperCase();'}),
                    'mold_code': forms.TextInput(attrs={'style':'text-transform: uppercase;','pattern':'^[0-9A-Za-z]+$;'}),
#                    'created_at': forms.DateInput(),
                    'created_at': datetimepicker.DatePickerInput(
#                        format='%Y-%m-%d',
                        options={
                            'format': 'Y-M-D',
                            'locale': 'ja',
                            'dayViewHeaderFormat': 'YYYY年 MMMM',
                        }
                    ),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }


# attrs={'onkeyup':'this.value = this.value.toUpperCase();'}
# attrs={'style':'text-transform: uppercase;'}
# attrs={'pattern':'^[0-9A-Za-z]+$;'}
	
#                    'code_a': forms.TextInput(attrs={'pattern':'^[A-Za-z0-9_@-]+$'}),
#                    'code_b': forms.URLInput(attrs={'style':'ime-mode: inactive;','inputmode':'url'}),
#                    'code_b': forms.TextInput(attrs={'onInput':'checkForm(this)'}),
