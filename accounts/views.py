from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account/login')
    else:
        form=UserCreationForm()

    args={'form':form}
    return render(request,'accounts/reg_form.html',args)

def profile(request):
    args={'user':request.user}
    return render(request, 'account/profile.html',args)
