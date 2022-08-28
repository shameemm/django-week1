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
        print("000",uname)
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
        pdt1.img='https://rukminim1.flixcart.com/image/312/312/xif0q/mobile/3/1/n/-original-imaggj686yhjdrgk.jpeg?q=70'
        pdt1.price=99999
        
        pdt2=Product()
        pdt2.name='APPLE iPhone 13 (Blue, 128 GB)'
        pdt2.description='Has a good camera, battery and price'
        pdt2.img='https://rukminim1.flixcart.com/image/416/416/ktketu80/mobile/2/y/o/iphone-13-mlpk3hn-a-apple-original-imag6vpyur6hjngg.jpeg?q=70'
        pdt2.price=65999
        
        pdt3=Product()
        pdt3.name='Nothing Phone (1) (Black, 128 GB)  (8 GB RAM)'
        pdt3.description='Has a good camera, battery and price on affordable price'
        pdt3.img='https://rukminim1.flixcart.com/image/416/416/l5h2xe80/mobile/5/x/r/-original-imagg4xza5rehdqv.jpeg?q=70'
        pdt3.price=33999
        
        pdts=[pdt1,pdt2,pdt3]
        return render(request, 'home.html',{'pdts':pdts})
    else:
        return redirect(to='login')

def logout(request):
    request.session.flush()
    return redirect(to='login')
