from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Todo title'}),
        label=""
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add a description...'}),
        required=False,
        label=""
    )

    class Meta:
        model = Todo
        fields = ['title', 'description']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'})) 