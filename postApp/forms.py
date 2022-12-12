from django import forms


class PostForm(forms.Form):
    header = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form--title'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form--content'}))
    is_publish = forms.BooleanField(label='Опубликовать', required=False)
    date = forms.CharField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
