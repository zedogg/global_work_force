from django.shortcuts import render
from mainlogin.models import Login

# Create your views here.
def home(request):
    return render(request,'hr_home.html')
def approval(request):
    data=Login.objects.all()
    if request.method=='POST':
        if 'approve' in request.POST:
            user=request.POST.get('approve')
            Login.objects.filter(user_name=user).update(approval='1')
        elif 'reject' in request.POST:
            user=request.POST.get('reject')
            Login.objects.filter(user_name=user).update(approval='0')


    return render(request,'hr_approval.html',{'data':data})