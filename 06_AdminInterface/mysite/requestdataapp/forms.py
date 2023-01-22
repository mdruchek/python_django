from django import forms


class UserBioForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    age = forms.IntegerField(label='Ваш возраст')
    bio = forms.CharField(label='Биография', widget=forms.Textarea)


class UploadFileForm(forms.Form):
    file = forms.FileField()
