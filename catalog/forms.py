from django import forms
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product, Blog, Version

EXCLUTION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('slug', 'count_views',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        cnt = 0
        for item in EXCLUTION_WORDS:
            if item == cleaned_data.lower():
                cnt += 1

        if cnt > 0:
            raise forms.ValidationError("слово запрещено")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'Some help text for field'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        cnt = 0
        for item in EXCLUTION_WORDS:
            if item == cleaned_data.lower():
                cnt += 1

        if cnt > 0:
            raise forms.ValidationError("слово запрещено")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'Some help text for field'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = 'Some help text for field'