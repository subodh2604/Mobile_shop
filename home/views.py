from django.shortcuts import render,redirect,get_object_or_404
from .models import signupit,mobile_spec,cart,buy_mobiles
from django.contrib.auth import login,logout
from django.contrib.auth.models import auth,User

# Create your views here.
def home(request):
    mobiles=mobile_spec.objects.all()
    print(mobiles)
    return render(request,'ECommerce/homepage.html',{'mobiles':mobiles})

def signup(request):
    if request.method=='GET':
        return render(request,'ECommerce/signup.html')
    else:
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        auth.login(request,user)
        return render(request,'ECommerce/homepage.html')

def login(request):
    if request.method=='GET':
        return render(request,'ECommerce/login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            return render(request,'ECommerce/login.html',{'error':'invalid'})

def logout(request):
    auth.logout(request)
    return redirect('home')

def specifications(request,mobile_pk):
        mobile=mobile_spec.objects.filter(pk=mobile_pk)
        return render(request,'ECommerce/specifications.html',{'mobile':mobile})

def carts(request):
    if request.method=='GET':  
        mobiles=cart.objects.filter(user=request.user)
        mlist=[]
        for mobile in mobiles:
            m1=mobile.cart_models.all()
            print('This is m1',m1)
            for m3 in m1:
                print('This is m3: ',m3)
                m2=mobile_spec.objects.all()
                for m in m2:
                    print('This is m:',m)
                    if m==m3:
                        print('matched')
                        mlist.append(m)
                        print(mlist)
                        #if m not in mlist:
                         #   mlist.insert(m)           
        return render(request,'Ecommerce/cart.html',{'mlist':mlist})  

def add_to_cart(request,addmobile_pk):
    m4=mobile_spec.objects.filter(pk=addmobile_pk)
    print(m4)
    a1=cart(user=request.user)
    a1.save()
    p1=a1.cart_models.set(m4)
    return redirect('home')

def remove_from_cart(request,remove_mobile_pk):
    if request.method=='POST':
        m5=cart.objects.filter(user=request.user)
        m6=mobile_spec.objects.filter(pk=remove_mobile_pk)
        for m7 in m5:  
            m8=m7.cart_models.all()
            for m9 in m8:
                for m10 in m6:
                    print('this is m8',m8)
                    print('this is m6',m6)
                    print('this is m9',m9)
                    print('this is m10',m10)
                    if m10.model==m9.model:
                        print('matched delete it',m7)
                        m7.delete()
        return redirect('home')

def buy_now(request,buy_pk):
        mobile=mobile_spec.objects.filter(pk=buy_pk)
        return render(request,'ECommerce/buy_now.html',{'mobile':mobile})

def buy(request,order_pk):
    if request.method=='POST':
        m4=mobile_spec.objects.filter(pk=order_pk)
        print(m4)
        quantity1=request.POST.get('quantity')
        address1=request.POST.get('address')
        print('quantity',quantity1)
        print('address',address1)
        order=buy_mobiles(quantity=quantity1,address=address1,user=request.user)
        order.save()
        order1=order.cart_models.set(m4)
        return redirect('home')

def search(request):
    search=request.POST.get('search')
    m3=mobile_spec.objects.filter(model=search)
    print(m3)
    if m3.exists() :
        print('none')
        return render(request,'ECommerce/homepage.html',{'m3':m3})
    else:
        return render(request,'ECommerce/homepage.html',{'error':'page not found'})
 




