from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mb-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
                'placeholder': 'Enter your post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 mb-4 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600',
                'placeholder': 'Write your post content here...',
                'rows': 6
            }),
        }
