from django.shortcuts import get_object_or_404 ,render
from django.urls import reverse
from . models import Producto
from . models import Categoria
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.order_by('nombre')[:4]
    context = {'product_list':product_list,
               'categoria_list':categoria_list
               }
    return render(request,'index.html',context)




def categoria(request,categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria_list = Categoria.objects.order_by('nombre')[:4]
    product_list = categoria.producto_set.all()
    context = {
                'product_list': product_list,
                'categoria_list':categoria_list
        }
    return render(request,'index.html',context)

def producto(request,producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    return render(request,'producto.html',{'producto':producto})


