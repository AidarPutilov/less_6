from django import forms
from django.db.models import BooleanField

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'preview', 'category', 'price', 'in_stock',)
        # exclude = ('in_stock',)

    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                       'бесплатно', 'обман', 'полиция', 'радар')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in self.forbidden_words:
            raise forms.ValidationError('Ошибка: в названии имеется запрещённое слово')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        if cleaned_data.lower() in self.forbidden_words:
            raise forms.ValidationError('Ошибка: в описании имеется запрещённое слово')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
