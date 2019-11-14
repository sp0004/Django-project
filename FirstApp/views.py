from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
def home(request):
    pets = Pet.objects.all()
    #return HttpResponse('<p> hello worlds </p>',,{'pets': pets})
    return render(request, 'home.html', {'pets': pets})
    
def pet_detail(request,id):
    #return HttpResponse('<p> pet detail with id {}</p>'.format(id))
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})

