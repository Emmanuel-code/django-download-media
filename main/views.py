from django.shortcuts import render,HttpResponse
from .forms import DownloadForm

import pytube
from pytube import Playlist


def home_view(request):
    context = {}
    form = DownloadForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        youtube = pytube.YouTube(str(form))
        youtube.streams.filter(progressive=True).order_by('resolution')
        download = youtube.streams.get_highest_resolution().download()  # "D:\YOUTUBE\Gabrysia"

        # playlist=Playlist("https://www.youtube.com/playlist?list=PLynhp4cZEpTbRs_PYISQ8v_uwO0_mDg_X")
        print(youtube.watch_url)
        context['youtube'] = youtube
        context['d'] = download
    context['form'] = form

    return render(request, "home.html", context)

