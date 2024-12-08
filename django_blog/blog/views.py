from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout


class HomeView(View):

    def get(self,request):
        user = self.request.user
        return render(request,'home.html',{'user':user})

class RegisterView(View):

    def get(self,request):
        form = CustomUserCreationForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        return render(request,'register.html',{'form':form})
    
def logout_view(request):
    logout(request)
    return render(request,'logout.html')