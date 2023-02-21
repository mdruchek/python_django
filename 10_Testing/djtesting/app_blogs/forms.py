from django import forms
from .models import BlogImage


class UploadFileForm(forms.Form):
    file_csv = forms.FileField()


class BlogCreateForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = BlogImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
