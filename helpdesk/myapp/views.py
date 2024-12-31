from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login,authenticate
from django.contrib import messages

def BasePage(request):
    return render(request,'base.html') 

# ini logic buat login
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Selamat akun Anda berhasil masuk!")
                return render(request,'base.html')
            else:
                messages.error(request, "Password atau username ada yang salah, coba periksa lagi")
                return render(request,'Login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'Login.html',{'form':form})
