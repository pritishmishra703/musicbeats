from django.shortcuts import render
from musicbeats.models import Song
from musicbeats.models import Watchlater
from django.db.models import Case, When

def index(request):
    song = Song.objects.all()[0:3]
    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    watch = Song.objects.filter(song_id__in=ids).order_by(preserved) 
    watch = reversed(watch)
    return render(request, 'index.htm', {'song': song, 'watch': watch})
