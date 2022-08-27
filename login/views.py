from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def login(request):
    if 'uname' in request.session:
        return redirect(to='home')
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        if uname == 'admin' and password == 'admin':
            request.session['uname'] = uname
            print("=======",request.session['uname'])
            return render(request, 'home.html')
        else:
            messages.info(request,'Enter Valid username and password')
            return render(request, 'login.html')
    else:   
        return render(request, 'login.html')

def home(request):
    if 'uname' in request.session:
        return render(request, 'home.html')
    else:
        return redirect(to='login')

def logout(request):
    request.session.flush()
    return redirect(to='login')
