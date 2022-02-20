from django.http import HttpResponse
from django.shortcuts import redirect, render
from.models import item
from.forms import itemform
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#Create your views here.
class additems(CreateView):
    model=item
    fields=['itemname', 'itemprice', 'itemdesc', 'itemimage']
    template_name='food/additems.html'

    def form_valid(self, form):
        form.instance.username=self.request.user
        return super().form_valid(form)

@login_required
def deleteitem(request, itemid):    
    items=item.objects.get(pk=itemid)       
    if request.method == 'POST':
        items.delete() 
        return redirect('index')
    return render(request, 'food/deleteitem.html', {'items':items})
             
@login_required    
def edititem(request, itemid):
    items=item.objects.get(pk=itemid)
    form=itemform(request.POST or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'food/additems.html', {'items':items, 'form':form})
    
# def additems(request):
#     form=itemform(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     else:
#         return render(request, 'food/additems.html', {'form':form})

def detail(request, itemid):
    items=item.objects.get(pk=itemid)    
    context={'items':items}  
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/detail.html', context)

def index(request):
    items=item.objects.all() 
    items_search=request.GET.get('items_search')
    if items_search != '' and items_search is not None:
        items=items.filter(itemname__icontains=items_search)   
    paginator=Paginator(items, 3)    
    page=request.GET.get('page')
    items=paginator.get_page(page)
    return render(request, 'food/index.html', {'items':items})

def items(request):
    items=item.objects.all()
    return HttpResponse('Items Page')