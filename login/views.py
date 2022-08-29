from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Product
user='admin'
pswd='admin'
# Create your views here.
def login(request):
    if 'uname' in request.session:
        return redirect(to='home')
    if request.method == 'POST':
        
        uname = request.POST['uname']
        password = request.POST['password']
        if len(uname)==0 and len(password)==0:
            messages.info(request,'Enter Valid username and password')
            return render(request, 'login.html')
        else:
            if uname == user:
                if password == pswd:
                    print
                    request.session['uname'] = uname
                    return redirect(to='home')
                else:
                    psmsg = 'Password is incorrect'
                    return render(request, 'login.html', {'psmsg':psmsg})
            else:
                unmsg = 'Username is incorrect'
                return render(request, 'login.html', {'unmsg':unmsg})
                
            
        
        # if uname == user and password == password:
        #     request.session['uname'] = uname
            
        #     return redirect(to='home')
        # else:
        #     messages.info(request,'Enter Valid username and password')
            
        #     return render(request, 'login.html',)
    else:   
        return render(request, 'login.html')

def home(request):
    if 'uname' in request.session:
        pdt1=Product()
        pdt1.name='SAMSUNG Galaxy S22 5G (Green, 128 GB)  (8 GB RAM)'
        pdt1.description='Good smart phone from Samsung. It gives good Battery.'
        pdt1.img='https://m.media-amazon.com/images/I/411WOa1yKoL._AC_UY218_.jpg'
        pdt1.price=99999
        
        pdt2=Product()
        pdt2.name='APPLE iPhone 13 (Blue, 128 GB)'
        pdt2.description='Has a good camera, battery and price'
        pdt2.img='https://m.media-amazon.com/images/I/71xb2xkN5qL._AC_UY218_.jpg'
        pdt2.price=65999
        
        pdt3=Product()
        pdt3.name='Nothing Phone (1) (Black, 128 GB)  (8 GB RAM)'
        pdt3.description='Has a good camera, battery and price on affordable price'
        pdt3.img='https://m.media-amazon.com/images/I/610PPZVHjvL._AC_UY218_.jpg'
        pdt3.price=33999
        
        pdts=[pdt1,pdt2,pdt3]
        return render(request, 'home.html',{'pdts':pdts})
    else:
        return redirect(to='login')

def logout(request):
    request.session.flush()
    return redirect(to='login')
