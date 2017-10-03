from django.http import HttpResponse
from .models import Album

#index and detail is a function, we can write anything we want, but make sure it is consisntent when used at other places
    #basically every view function is going to take the request. The request is HTML request, when user connect to your site, and request for smth. There are several background info too such as their IP address, etc
#request is bsaically when a user request for smth
#album_id is a variable, also appeared in admin
def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href ="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")