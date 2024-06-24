from django.shortcuts import render,get_object_or_404
from .models import Campaign, Category, Product
from django.db.models import Count
def home(request):
    
    slide_campaigns=Campaign.objects.filter(is_slide=True)[:3]
    nonslide_campaigns=Campaign.objects.filter(is_slide=False)[:4]
    categories=Category.objects.annotate(product_count=Count('products'))
    featured_products=Product.objects.filter(featured=True)[:8]
    recent_products=Product.objects.all().order_by('-created')[:8]
    return render(request,'home.html',{
        'slide_campaigns':slide_campaigns,
        'nonslide_campaigns':nonslide_campaigns,
        'categories':categories,
        'featured_products':featured_products,
        'recent_products':recent_products

    })


def shop(request):
    return render (request,'shop.html')

def shop_detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    others_products=Product.objects.exclude(pk=product.pk).order_by('?')[:5]
    return render(request,'product-detail.html',{
        'product':product,
        'others_products':others_products,
    })
