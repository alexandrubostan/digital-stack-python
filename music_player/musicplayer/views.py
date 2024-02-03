from django.http import HttpResponse
from django.shortcuts import render
import requests
import os
from .models import Song

def player(request):
    return render(request, 'player.html')

def postRequest(request):
    thefile = request.FILES['thefile']
    string = thefile.name
    artistname = string.split(" - ")[0]
    artistname = artistname.replace(" ", "%20")
    songname = os.path.splitext("".join(string.split(" - ")[1:]))[0]
    songname = songname.replace(" ", "%20")
    urlstring = 'https://api.lyrics.ovh/v1/' + artistname + '/' + songname
    response = requests.get(urlstring)
    responsejson = response.json()
    if response.status_code == 200:
        for key in responsejson:
            responsejson = responsejson[key]
    else:
        responsejson = 'Lyrics not found'
    return HttpResponse(responsejson)

def saveRequest(request):
    thefile = request.FILES['thefile']
    string = thefile.name
    artistname = string.split(" - ")[0]
    songname = os.path.splitext("".join(string.split(" - ")[1:]))[0]
    song = Song(Name=songname, Artist=artistname, Size=thefile.size, RawData=thefile.read())
    song.save()
    return HttpResponse("Save")
