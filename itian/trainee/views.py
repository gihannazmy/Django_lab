from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def trainees_list(request):
    trainees = [
        {
            "id": 1,
            "name": "Safa",
            "age": 22,
            "email": "safa.abduallah2001@hotmail.com",
            "department": "Backend",
        },
        {
            "id": 2,
            "name": "Ahmed",
            "age": 24,
            "email": "ahmed.suli@gmail.com",
            "department": "Admin01",
        },
        {
            "id": 3,
            "name": "Helana",
            "age": 25,
            "email": "helana.nabil@gmail.com",
            "department": "ClientSide",
        },
    ]
    context = {}
    context["trainees"] = trainees
    return render(request, "trainee/tranieesList.html", context)
    # return HttpResponse("<h2>Trainees List</h2>")


def create_trainee(request):
    # return HttpResponse("<h1>Create Trainee</h1>")
    return render(request, "trainee/createTrainee.html")


def update_trainee(request, id):
    # return HttpResponse("<h2>Update Trainee</h2>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/updateTrainee.html", context)


def delete_trainee(request, id):
    # return HttpResponse("<h2>Delete Trainee</h2>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/deleteTrainee.html", context)


def trainees_details(request, id):
    # return HttpResponse(f"<h2>Trainees Details: {id}</h2>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/traineeDetails.html", context)