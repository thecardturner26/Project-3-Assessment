from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item




# Create your views here.
def home(request):
  return render(request, 'home.html')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'






# def add(request):
#     return render(request, 'add.html')

# def add(request):
#     if request.method == 'POST':
#         if request.POST.get('description'):
#             item=Item()
#             item.description= request.POST.get('description')
#             item.save()
                
#             return render(request,'add.html')  

#         else:
#             return render(request,'add.html')
