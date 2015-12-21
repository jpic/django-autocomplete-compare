from django import forms

from django_select2.forms import ModelSelect2Widget
import autocomplete_light.shortcuts as al

from .models import Item


class S2ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'parent')
        widgets = {
            'parent': ModelSelect2Widget(
                model=Item,
                search_fields=['name__icontains']
            ),
        }


class AlItemForm(al.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'parent')
