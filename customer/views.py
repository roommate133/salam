from django.shortcuts import render,redirect
from .forms import ContactForm,RegisterForm
from django.contrib.auth import login,authenticate,logout
app_name='customer'
def basket(request):
    return render(request,'basket.html')
def contact(request):
    form=ContactForm
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html',{'form':form , 'results':'success'})
        return render(request, 'contact.html',{'form':form , 'results':'fail'})
        
    return render(request,'contact.html',context={'form':form})

def register(request):
    form=RegisterForm
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            customer=form.save()
            login(request,customer.user)    
            return redirect('shop:home')
    return render(request,'register.html',context={'form':form})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:home')
        return render(request,'login.html',{'fail':True})
    return render(request,'login.html',{})


def logout_view(request):
    logout(request)
    return redirect('customer:login')