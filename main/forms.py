from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter a new todo...'}),
        label=""
    )

    class Meta:
        model = Todo
        fields = ['title']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea) 