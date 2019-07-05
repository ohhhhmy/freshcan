from django.shortcuts import render, get_object_or_404, redirect
from .models import Vegetable, Meat, Fruit, Grain, Seafood, Information
from .forms import InformationForm
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def vegetable(request):
    vegetables = Vegetable.objects
    return render(request, 'vegetable/vegetable.html', {'vegetables' : vegetables})

def meat(request):
    meats = Meat.objects
    return render(request, 'meat/meat.html', {'meats' : meats})

def fruit(request):
    fruits = Fruit.objects
    return render(request, 'fruit/fruit.html',{'fruits':fruits})

def grain(request):
    grains = Grain.objects
    return render(request, 'grain/grain.html',{'grains':grains})

def seafood(request):
    seafoods = Seafood.objects
    return render(request, 'seafood/seafood.html',{'seafoods':seafoods})


def fpost(request):
    if request.method == "POST":
        form = InformationForm(request.POST) 

        if form.is_valid(): 
            information = form.save(commit=False) 
            information.update_date=timezone.now() 
            information.save()
            return redirect('fshow') 
    else:
        form = InformationForm() 
        return render(request, 'fpost.html',{'form' : form})

def fshow(request):
        informations = Information.objects.order_by('-id')
        return render(request, 'fshow.html', {'informations':informations})

def edit(request, pk):
        information = get_object_or_404(Information, pk=pk)

        if request.method == "POST":
                form = InformationForm(request.POST, instance=information) 

                if form.is_valid(): 
                        information = form.save(commit=False) 
                        information.update_date=timezone.now() 
                        information.save()
                        return redirect('fshow') 

        else:
                form = InformationForm(instance=information) 
                return render(request, 'edit.html',{'form' : form})

def delete(request, pk):
        information = Information.objects.get(id=pk)
        information.delete()
        return redirect('fshow')



