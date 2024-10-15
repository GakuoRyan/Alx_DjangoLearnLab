# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Fields to be included in the form

        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add your comment here...'}),
        }
# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from django import forms
from .models import Post, Tag


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

from django import forms
from .models import Post, Tag
from .widgets import TagWidget()  # Import your custom widget

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=TagWidget,
        required=False
    )

class TagWidget(forms.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


