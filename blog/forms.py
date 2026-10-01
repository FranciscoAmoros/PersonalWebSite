from django import forms
from .models import Comment

from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {"text": "Comentario"}
        widgets = {"text": forms.Textarea(attrs={"rows": 4})}