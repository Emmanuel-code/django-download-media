from django import forms


class DownloadForm(forms.Form):
    youtube_url = forms.CharField(max_length=100)
