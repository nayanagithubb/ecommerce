from fnmatch import fnmatchcase
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from ecommerceapp.models import Category,Product,Usermember,Cart
import os
# Create your views here.
def home(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')
    
def admin_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('admin_home')
            
         
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('user_home')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
    return render(request,'home.html')
    
def admin_home(request):
    if request.user.is_authenticated:
        return render(request,'adminhome.html')
    return render(request,'home.html')
    
def admin_logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')

def add_category(request):
        category=Category.objects.all()
        return render(request,'addcategory.html',{'category':category})
    

def add_categorydb(request,cat_id):
    if request.method=="POST":
        category=request.POST.get('category')
        category=Category(category=category)
        category.save()
        return redirect('add_category')
    else:
        if cat_id:
            category=Category.objects.get(id=cat_id)
            products=Product.objects.filter(category=category)
            return render(request,'showcategory.html',{'category':category,'products':products})
        else:
            return redirect('add_category')
        
def show_category(request):
    return render(request,'showcategory.html')

def add_product(request):
    if request.user.is_authenticated:
        category=Category.objects.all()
        return render(request,'addproduct.html',{'category':category})
    return redirect('/')


def add_productdb(request):
    if request.method=='POST':
        productname=request.POST['productname']
        print(productname)
        description=request.POST['description']
        print(description)
        sel=request.POST['sel']
        print(sel)
        category1=Category.objects.get(id=sel)
        print(category1)
        price=request.POST['price']
        print(price)
        quantity=request.POST['quantity']
        print(quantity)
        pimage=request.FILES.get('file')
        print(pimage)
        product=Product(productname=productname,description=description,category=category1,price=price,quantity=quantity,pimage=pimage)
        product.save()
        return redirect('add_product')

def show_product(request):
    if request.user.is_authenticated:
        product=Product.objects.all()
        return render(request,'showproduct.html',{'products':product})
    return redirect('/')       

def delete_page(request,pk): 
    product=Product.objects.get(id=pk) 
    product.delete()
    return redirect('show_product')

def signuppage(request):
    return render(request,'usersignup.html')
    
def add_userdb(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        address=request.POST.get('address')
        number=request.POST.get('number')
        email=request.POST.get('email')
        image=request.FILES.get('file')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
                user.save()
                u=User.objects.get(id=user.id)
            
                member=Usermember(address=address,number=number,image=image,user=u)
                member.save()
                # messages.info(request, 'You have successfully registered')
                return redirect('/')
            
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            
            return redirect('signuppage')         
        
    else:
        return render(request,'usersignup.html')
        
def user_home(request):
        usr=request.user
        user=Usermember.objects.get(user=usr)
        category=Category.objects.all()
        product=Product.objects.all()
        return render(request,'userhome.html',{'category':category,'products':product,'user':user})
        
    
def show_user(request):
    if request.user.is_authenticated:
        user1=Usermember.objects.all
        return render(request,'showuser.html',{'user':user1})
    return redirect('/')  

def delete(request,pk):
    user=Usermember.objects.get(id=pk)
    if user.image:
        user.image.delete()
    user.delete()
    user.user.delete()
    return redirect("show_user")  


  
def add_to_cart(request,pk):
    if request.user.is_authenticated:
        product=get_object_or_404(Product,id=pk)
        cartitem=Cart(user=request.user,product=product)
        cartitem.save()
        return redirect('cart')
    else:
        return redirect('add_categorydb')
    
def cart(request):
    usercart=Cart.objects.filter(user=request.user)  
    return render(request, 'cart.html',{'usercart':usercart})

def delete_cart(request,pk):     
    cartitem=Cart.objects.get(id=pk)
    cartitem.delete()
    return redirect('cart')


