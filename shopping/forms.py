from django.forms import ModelForm
from django import forms
from shopping.models import Shop


class FormShop(ModelForm):
  class Meta:
    model = Shop
    fields = '__all__'
    

    widgets = {
        'name' : forms.TextInput({'class':'form-control'}),
        'diskripsi' : forms.Textarea(attrs={'rows': 4}),
        'harga' : forms.NumberInput({'class':'form-control'}),
    }