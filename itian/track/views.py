from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def track_list(request):
    tracks = [
        {"id": 1, "name": "ClientSide", "description": "Html,JS, Css"},
        {"id": 2, "name": "Admin01", "description": "Ubuntu"},
        {"id": 3, "name": "BackEnd", "description": "Python, Django"},
    ]
    context = {}
    context["tracks"] = tracks
    return render(request, "track/trackList.html", context)
    # return HttpResponse("<h2>track List</h2>")


def create_track(request):
    # return HttpResponse("<h2>Create Track</h2>")
    return render(request, "track/createTrack.html")


def update_track(request, id):
    # return HttpResponse("<h2>Update Track</h2>")
    context = {}
    context = {"id": id}
    return render(request, "track/updateTrack.html", context)


def delete_track(request, id):
    # return HttpResponse("<h2>Delete Track</h2>")
    context = {}
    context = {"id": id}
    return render(request, "track/deleteTrack.html", context)


def track_detail(request, id):
    # return HttpResponse("<h2>Track Details: {id}</h2>")
    context = {}
    context = {"id": id}
    return render(request, "track/trackDetail.html", context)