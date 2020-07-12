from django import forms

class BlogForm(forms.Form):
    blog_text = forms.CharField(label='Blog Text', max_length=100)