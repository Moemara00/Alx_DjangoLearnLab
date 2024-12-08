from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomUserCreationForm ,CustomUserChangeForm,PasswordChangeForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ProfileView(LoginRequiredMixin,TemplateView):

        template_name= 'profile.html'

class ChangeView(View):
    def get(self,request):
        form = CustomUserChangeForm(instance=request.user)
        return render(request,'change.html',{'form':form})

    def post(self,request):
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request,'change.html',{'form':form})
    
class ChangePassword(View):
    def get(self,request):
        form = PasswordChangeForm(user=request.user)
        return render(request,'change_pass.html',{'form':form})

    def post(self,request):
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.warning(request,"Sorry the Password is weak try again!")
            return render(request,'change_pass.html',{'form':form})

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