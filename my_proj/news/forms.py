from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'title',
            'content',
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        if content is not None and len(content) < 20:
            raise ValidationError({
                'content': 'content length must be at least 20 symbols'
            })
        title = cleaned_data.get('title')
        if title == content:
            raise ValidationError(
                'content and title should differ'
            )
        return cleaned_data