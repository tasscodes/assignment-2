from django.shortcuts import render, redirect
from . models import Student
# Create your views here.
def index(request):
    std = Student.objects.all()
    context = {
        'std': std,
    }
    return render(request, 'index.html', context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        std = Student(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        std.save()
        return redirect('home')

    return render(request, 'index.html')

def edit(request):
    std = Student.objects.all()

    context = {
        'std':std,
    }
    return redirect(request, 'index.html',context)

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        std = Student(
            id = id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        std.save()
        return redirect('home')

    return redirect(request, 'index.html')


def delete(request, id):
    std = Student.objects.filter(id = id)
    std.delete()

    context = {
        'std': std,
    }
    return redirect('home')