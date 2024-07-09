from django.shortcuts import render,redirect
from .models import Login

# Create your views here.
def login(request):
    msg=' Login Credentials'
    if request.method=='POST':
        
        if 'sign_in' in request.POST:
           
            username=request.POST.get('username')
            password=request.POST.get('password')
            auth=Login.objects.filter(user_name=username,password=password)
           
            if auth:
                
                if auth[0].user_type=='1' and auth[0].approval=='1':

                    return redirect('/hr')
                elif auth[0].approval !='1':
                    msg='user not approved'
            else:
                auth=Login.objects.filter(user_name=username)
                if auth:
                    msg='Incorrect Password.'
                
                else:
                    msg='Invaliv Username'
                
        elif 'sign_up' in request.POST:
            return redirect('/register')
    
    return render(request,'login.html',{'message':msg})
def register(request):
    msg=''
    if request.method=='POST':
        user_name=request.POST.get('user_name')
        password=request.POST.get('password')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        user_type=request.POST.get('user_type')
        user=Login.objects.filter(user_name=user_name)
        if user:
            msg='Username already in use. Please try diffrent Username. '
        else:
            Login.objects.create( user_name=user_name, password=password, user_type=user_type, f_name=f_name, l_name=l_name,approval='0')
            msg='Registered Succesfuly !!'
    print(msg)    
    return render(request,'registration.html',{'message':msg})