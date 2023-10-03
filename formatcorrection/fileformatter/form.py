from django import forms


class FileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs = {'multiple':True}), allow_empty_file=True)