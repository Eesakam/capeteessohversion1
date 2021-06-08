from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .models import Product,NewItem
from .forms import NewItemForm,StockUpdateForm,SaleForm,NEWSTOCK
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


def HomePage(request):
    return render(request,"home.html")


def AddItem(request):
    form = NewItemForm()
    if request.method == "POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Succesfully added new item")
            return redirect("HomePage")

    return render(request,"additem.html",{"form":form})


def SOH(request):
    queryset = NewItem.objects.all().order_by("product_type","color","size")
    context = {"queryset": queryset}
    return render(request,"SOH.html",context)


def SearchItem(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(description__icontains=query)|Q(color__icontains=query)

            results= NewItem.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'home.html')



def update_stock(request,pk):
    queryset = NewItem.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == "POST":
        form = StockUpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request,"Succesfully updated item")
            return redirect("Capeteesstock:SOH")
    context = {
    "form":form}

    return render(request,"update_items.html",context)

def incoming(request,pk):
    queryset = NewItem.objects.get(id=pk)
    form = NEWSTOCK(request.POST)
    if request.method == "POST":
        if form.is_valid():
            newamount = int(request.POST['amount'])
            queryset.amount += newamount
            queryset.save()
            messages.success(request,"Succesfully added new incoming stock")
            return redirect("Capeteesstock:SOH")

    context = {"form":form}

    return render(request,"incoming.html",context)




def sale(request,pk):
    queryset = NewItem.objects.get(id=pk)
    form = SaleForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            newamount = int(request.POST['amount'])
            queryset.amount -= newamount
            queryset.save()

            return render(request,"home.html")
    context = {"form":form}
    return render(request,"sale.html",context)
