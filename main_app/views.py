from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, HttpResponseRedirect
from .models import Item




# Create your views here.
def home(request):
  return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        if request.POST.get('description'):
            return render(request, 'home.html')

# def add(request):
#     if request.method == 'POST':
#         if request.POST.get('description'):
#             item=Item()
#             item.description= request.POST.get('description')
#             item.save()
                
#             return render(request,'home.html')  

#         else:
#             return render(request,'add.html')
