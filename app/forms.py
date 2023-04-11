from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('department','name','frame_code','molds_code','molding_machine','frame_height_moving_side','number_of','weight','age','sex','memo','is_drawing',)
        widgets = {
                    'department': forms.TextInput(attrs={'placeholder':'記入例：焼津'}),
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎','onkeyup':'this.value = this.value.toUpperCase();'}),
                    'frame_code': forms.TextInput(attrs={'onkeyup':'this.value = this.value.toUpperCase();'}),
                    'molds_code': forms.TextInput(attrs={'style':'text-transform: uppercase;','pattern':'^[0-9A-Za-z]+$;'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                    'is_drawing': forms.CheckboxInput(),
                  }


# attrs={'onkeyup':'this.value = this.value.toUpperCase();'}
# attrs={'style':'text-transform: uppercase;'}
# attrs={'pattern':'^[0-9A-Za-z]+$;'}

	
