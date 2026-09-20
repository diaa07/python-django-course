from django import forms
from .models import Category
from django.core.exceptions import ValidationError


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name or not name.strip():
            raise ValidationError(
                "Name can't be empty or consist of whitespaces only!")
        name = name.strip()

        query = Category.objects.filter(name__iexact=name)

        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise ValidationError("Category already exists!")

        return name
