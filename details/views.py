from django.shortcuts import render ,redirect, get_object_or_404
from .models import Person
from django.utils.translation import activate
from django.conf import settings


# Create your views here.

def switch_language(request, lang_code):
    if lang_code in dict(settings.LANGUAGES):
        request.session['django_language'] = lang_code
        activate(lang_code)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def contact_details(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'don': persons})

def add_details(request):
    return render(request, 'add.html')

def store_details(request):
     if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        description = request.POST.get('message')
        person = Person( name = name, address = address, description = description)
        person.save()
        return render(request, 'add.html')

def edit_details(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, 'edit.html',{'sonu' : person})
    

def update_details(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == "POST":
        person.name = request.POST.get('name')
        person.address = request.POST.get('address')
        person.description = request.POST.get('message')
        person.save()
        return redirect('home')

    return render(request, 'edit.html', {'person': person})

def delete_details(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('home')
