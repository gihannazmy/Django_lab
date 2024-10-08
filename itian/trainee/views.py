from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def trainee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Trainee.objects.create(name=name, email=email)
        return redirect('trainee_list')
    return render(request, 'trainee/create_form.html')

def trainee_update(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/update_form.html', {'trainee': trainee})

def trainee_delete(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/delete_confirm.html', {'trainee': trainee})

def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/details.html', {'trainee': trainee})
