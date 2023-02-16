from django import forms


class UploadFileForm(forms.Form):
    file_csv = forms.FileField()
