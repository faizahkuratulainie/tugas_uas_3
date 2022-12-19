from django.shortcuts import render
from shopping.models import Shop
from shopping.forms import FormShop


def index(request):
    shop = Shop.objects.all()
    
    context = {
        "shop": shop,
    }
    return render(request, 'shop.html',context)

def update(request):
    if request.POST:
        form = FormShop(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormShop()
            pesan = "Produk Berhasil Ditambahkan"
            
    
            context = {
                'form': form,
                'pesan': pesan,
            }
            return render(request,'update.html',context)
    else:
        form = FormShop()
        
        context = {
            'form': form,
        }
        return render(request,'update.html',context)